# Setup
GRID_SIDE = 1000


# Read input
with open("input.txt", "r") as f:
    lines = f.readlines()


# Parse input
coordinates_temp = []

for line in lines:
    line.replace("\n", "")
    coordinates_temp.append(line.replace('\n', '').split(' -> '))
    
coordinates = [[0, 0] for _ in range(len(coordinates_temp))]

for line in range(len(coordinates_temp)):
    coordinates[line][0] = tuple(map(int, coordinates_temp[line][0].split(',')))
    coordinates[line][1] = tuple(map(int, coordinates_temp[line][1].split(',')))


# Functions
def is_horizontal(line):
    return line[0][0] == line[1][0]


def is_vertical(line):
    return line[0][1] == line[1][1]


def is_diagonal(line):
    # NE
    x = line[0][0]
    y = line[0][1]
    while x <= GRID_SIDE and x >= 0 and y <= GRID_SIDE and y >= 0:
        x = x + 1
        y = y + 1
        
        if x == line[1][0] and y == line[1][1]:
            return 'NE'

    # NW
    x = line[0][0]
    y = line[0][1]
    while x <= GRID_SIDE and x >= 0 and y <= GRID_SIDE and y >= 0:
        x = x - 1
        y = y + 1
        
        if x == line[1][0] and y == line[1][1]:
            return 'NW'

    # SW
    x = line[0][0]
    y = line[0][1]
    while x <= GRID_SIDE and x >= 0 and y <= GRID_SIDE and y >= 0:
        x = x - 1
        y = y - 1
        
        if x == line[1][0] and y == line[1][1]:
            return 'SW'

    # SE
    x = line[0][0]
    y = line[0][1]
    while x <= GRID_SIDE and x >= 0 and y <= GRID_SIDE and y >= 0:
        x = x + 1
        y = y - 1
        
        if x == line[1][0] and y == line[1][1]:
            return 'SE'

    return ''


# Task
grid = [[0 for _ in range(GRID_SIDE)] for _ in range(GRID_SIDE)]

for line in coordinates:
    if is_horizontal(line) or is_vertical(line):
        min_x = min(line[0][0], line[1][0])
        max_x = max(line[0][0], line[1][0])
        min_y = min(line[0][1], line[1][1])
        max_y = max(line[0][1], line[1][1])

        if min_x == max_x:
            for y in range(min_y, max_y + 1):
                grid[y][min_x] = grid[y][min_x] + 1
        elif min_y == max_y:
            for x in range(min_x, max_x + 1):
                grid[min_y][x] = grid[min_y][x] + 1
    else: 
        diagonality = is_diagonal(line)

        if diagonality != '':
            x = line[0][0]
            y = line[0][1]
            grid[y][x] = grid[y][x] + 1

            finished = False
            while not finished:
                if diagonality == 'NE':
                    x = x + 1
                    y = y + 1
                elif diagonality == 'NW':
                    x = x - 1
                    y = y + 1
                elif diagonality == 'SW':
                    x = x - 1
                    y = y - 1
                elif diagonality == 'SE':
                    x = x + 1
                    y = y - 1

                grid[y][x] = grid[y][x] + 1

                if x == line[1][0]:
                    finished = True
            

sum = 0
for i in grid:
    for j in i:
        if j > 1:
            sum = sum + 1

print(sum)