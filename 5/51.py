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


# Task
grid = [[0 for _ in range(1000)] for _ in range(1000)]

for line in coordinates:
    if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
        min_x = min(line[0][0], line[1][0])
        max_x = max(line[0][0], line[1][0])
        min_y = min(line[0][1], line[1][1])
        max_y = max(line[0][1], line[1][1])

        if min_x == max_x:
            for i in range(min_y, max_y + 1):
                # print(min_x, max_x, min_y, max_y, i)
                grid[min_x][i] = grid[min_x][i] + 1
        else:
            for i in range(min_x, max_x + 1):
                # print(min_x, max_x, min_y, max_y, i)
                grid[i][min_y] = grid[i][min_y] + 1


sum = 0
for i in grid:
    for j in i:
        if j > 1:
            sum = sum + 1

print(sum)