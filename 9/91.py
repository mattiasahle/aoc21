# Read input
with open("input.txt", "r") as f:
    l = f.readlines()


# Parse input
l = [i.replace("\n", "") for i in l]
locations = [list(map(int, [c for c in line])) for line in l]


# Main
risk_levels_sum = 0

for row in range(len(locations)):
    for column in range(len(locations[row])):
        temp_list = []
        number = locations[row][column]

        N = [row - 1, column]
        S = [row + 1, column]
        E = [row, column + 1]
        W = [row, column - 1]

        if N[0] >= 0: temp_list.append(locations[N[0]][N[1]])
        if S[0] < len(locations): temp_list.append(locations[S[0]][S[1]])
        if E[1] < len(locations[row]): temp_list.append(locations[E[0]][E[1]])
        if W[1] >= 0: temp_list.append(locations[W[0]][W[1]])

        if number < min(temp_list):
            risk_levels_sum = risk_levels_sum + number + 1


print(risk_levels_sum)