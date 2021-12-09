# INFO
# r = row
# c = column

import math

# Read input
with open("input.txt", "r") as f:
    l = f.readlines()

# Parse input
l = [i.replace("\n", "") for i in l]
locations = [list(map(int, [c for c in line])) for line in l]


# Functions
def get_bearings(r, c):
    return [r - 1, c], [r + 1, c], [r, c + 1], [r, c - 1] 


def check_low_point(N, S, E, W, number, temp_list):
    if N[0] >= 0: temp_list.append(locations[N[0]][N[1]])
    if S[0] < len(locations): temp_list.append(locations[S[0]][S[1]])
    if E[1] < len(locations[r]): temp_list.append(locations[E[0]][E[1]])
    if W[1] >= 0: temp_list.append(locations[W[0]][W[1]])

    return number < min(temp_list)


def check_north(r, c):
    if r >= 0 and locations[r][c] != 9 and locations[r][c] != '.' and locations[r][c] != ' ':
        locations[r][c] = '.'
        basin_sum = 1 + check_north(r - 1, c)
        basin_sum = basin_sum + check_east(r, c + 1)
        basin_sum = basin_sum + check_west(r, c - 1)
        return basin_sum
    else:
        return 0


def check_south(r, c):
    if r < len(locations) and locations[r][c] != 9 and locations[r][c] != '.' and locations[r][c] != ' ':
        locations[r][c] = '.'
        basin_sum = 1 + check_south(r + 1, c)
        basin_sum = basin_sum + check_east(r, c + 1)
        basin_sum = basin_sum + check_west(r, c - 1)
        return basin_sum
    else:
        return 0


def check_east(r, c):
    if c < len(locations[r]) and locations[r][c] != 9 and locations[r][c] != '.' and locations[r][c] != ' ':
        locations[r][c] = '.'
        basin_sum = 1 + check_east(r, c + 1)
        basin_sum = basin_sum + check_north(r - 1, c)
        basin_sum = basin_sum + check_south(r + 1, c)
        return basin_sum
    else:
        return 0


def check_west(r, c):
    if c >= 0 and locations[r][c] != 9 and locations[r][c] != '.' and locations[r][c] != ' ':
        locations[r][c] = '.'
        basin_sum = 1 + check_west(r, c - 1)
        basin_sum = basin_sum + check_north(r - 1, c)
        basin_sum = basin_sum + check_south(r + 1, c)
        return basin_sum
    else:
        return 0


def add_to_basins(basin):
    if len(basins) < 3:
        basins.append(basin)
    elif basin > min(basins):
        for i in range(len(basins)):
            if basins[i] == min(basins):
                basins[i] = basin
                break
    else:
        return


# Main
basins = []


for r in range(len(locations)):
    for c in range(len(locations[r])):
        temp_list = []
        value = locations[r][c]

        if value != '.' and value != 9:
            N, S, E, W = get_bearings(r, c)
            is_low_point = check_low_point(N, S, E, W, value, temp_list)

            if is_low_point:
                locations[r][c] = ' '
                basin = 1 + check_north(N[0], N[1])
                basin = basin + check_south(S[0], S[1])
                basin = basin + check_east(E[0], E[1])
                basin = basin + check_west(W[0], W[1])
                add_to_basins(basin)


# print(basins)
# print(math.prod(basins))

for i in locations:
    for j in i:
        print(j, end='')
    print()