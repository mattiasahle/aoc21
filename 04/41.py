with open("input.txt", "r") as f:
    draw = f.readline()
    boards_raw = f.readlines()


# Create draw list of integers
draw = list(map(int, draw.replace("\n", "").split(",")))


# Create list of boards
board = []
boards = []

for line in boards_raw:
    # print(line)
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
            print("Row BINGO!")
            return True
        else:
            column_sum = column_sum + register[board][row][column]
            if column_sum == 5:
                print("Column BINGO!")
                return True

    return False


# Play Bingo
is_bingo = False
winning_board = -1
winning_draw = -1

for number in draw:
    board, row, index = 0, 0, 0
    for board in range(len(boards)):
        for row in range(len(boards[board])):
            for index in range(len(boards[board][row])):
                if number == boards[board][row][index]:
                    register[board][row][index] = 1
                    is_bingo = check_if_bingo(board, index)
                if is_bingo:
                    winning_board = board
                    winning_draw = number
                    break
            if is_bingo: break
        if is_bingo: break
    if is_bingo: break


# Calculate sum of unmarked numbers
sum = 0

for row in range(5):
    for index in range(5):
        if register[winning_board][row][index] == 0:
            sum = sum + boards[winning_board][row][index]


# print_boards()
# print_register()
print('Winning board: ', winning_board)
print('Winning draw: ', winning_draw)
print('Sum: ', sum)

print('Answer: ', sum * winning_draw)