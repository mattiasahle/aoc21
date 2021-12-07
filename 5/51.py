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


# Remove non-horizontal or non-vertical lines
i = 1
for line in coordinates:
    if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
        coordinates.remove(line)
        print(i, line)
        i = i + 1

print(len(coordinates))