with open("input.txt", "r") as f:
    draw = f.readline()
    boards_raw = f.readlines()

draw = list(map(int, draw.replace('\n', '').split(',')))

board = []
boards = []

for line in boards_raw:
    if line != '\n':
        line.replace('\n', '')
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

