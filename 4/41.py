with open("input.txt", "r") as f:
    draw = f.readline()
    boards_raw = f.readlines()

draw = list(map(int, draw.replace("\n", "").split(",")))

board = []
boards = []

for line in boards_raw:
    if line != "\n":
        line.replace("\n", "")
        board.append(list(map(int, line.split())))
    else:
        boards.append(board)
        board = []

boards.pop(0)

# Print boards
# for board in boards:
#     for row in board:
#         print(row)
#     print()

# Create empty register
register = []
for board in range(len(boards)):
    register.append([])
    for row in range(len(boards[board])):
        register[board].append([])
        for index in range(len(boards[board][row])):
            register[board][row].append(0)


def print_register():
    for board in register:
        for row in board:
            print(row)
        print()


def is_bingo(board):
    for row in board:
        if sum(row) == 5:
            print("BINGO!")

            return True

    return False


# Play Bingo
for number in draw[0:4]:
    board, row, index = 0, 0, 0
    for board in range(len(boards)):
        for row in range(len(boards[board])):
            for index in range(len(boards[board][row])):
                if number == boards[board][row][index]:
                    register[board][row][index] = 1

        if is_bingo(boards[board]):
            break

# print_register()
