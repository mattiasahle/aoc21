with open("input.txt", "r") as f:
    draw = f.readline()
    boards_raw = f.readlines()


# Create draw list of integers
draw = list(map(int, draw.replace("\n", "").split(",")))


# Create list of boards
board = []
boards = []

for line in boards_raw:
    if line != "\n":
        line.replace("\n", "")
        board.append(list(map(int, line.split())))
    else:
        boards.append(board)
        board = []

boards.append(board)
boards.pop(0)

def print_boards():
    for board in range(len(boards)):
        print(board)
        for row in boards[board]:
            print(row)
        print()


# Create empty mark register
register = []
for board in range(len(boards)):
    register.append([])
    for row in range(len(boards[board])):
        register[board].append([])
        for index in range(len(boards[board][row])):
            register[board][row].append(0)


def print_register():
    for board in range(len(register)):
        print(board)
        for row in register[board]:
            print(row)
        print()


def check_if_bingo(board, column):
    column_sum = 0

    for row in range(len(register[board])):
        if sum(register[board][row]) == 5:
            return True
        else:
            column_sum = column_sum + register[board][row][column]
            if column_sum == 5:
                return True

    return False


# Play Bingo
bingo_register = [False for _ in boards]
nr_of_bingos = len(bingo_register)
is_bingo = False
losing_board = -1
losing_draw = -1
finished = False

for number in draw:
    board, row, index = 0, 0, 0
    for board in range(len(boards)):
        for row in range(len(boards[board])):
            for index in range(len(boards[board][row])):
                if number == boards[board][row][index]:
                    register[board][row][index] = 1
                    is_bingo = check_if_bingo(board, index)
                if is_bingo and bingo_register[board] == False:
                    bingo_register[board] = True
                    nr_of_bingos = nr_of_bingos - 1
                    if nr_of_bingos == 0:
                        losing_board = board
                        losing_draw = number
                        finished = True
                        break
                else:
                    is_bingo = False
                if finished: break 
            if finished: break
        if finished: break
    if finished: break


# Calculate sum of unmarked numbers
sum = 0

for row in range(5):
    for index in range(5):
        if register[losing_board][row][index] == 0:
            sum = sum + boards[losing_board][row][index]


# print_boards()
print_register()
print(bingo_register)
print('Losing board: ', losing_board)
print('Losing draw: ', losing_draw)
print('Sum: ', sum)

print('Answer: ', sum * losing_draw)