# Read input
with open("input.txt", "r") as f:
    l = f.readlines()


# Parse input
l = [i.replace("\n", "") for i in l]
locations = [list(map(int, [c for c in line])) for line in l]


# Main
risk_levels = 0

# for i in range(len(locations[0:1])):
#     for j in range(len(locations[i][0:1])):
#         temp_list = []
#         if i == 0 and j == 0:
#             temp_list.append(locations[i + 1][j])
#             temp_list.append(locations[i][j - 1])
#         print(temp_list)

i = 0
j = 0
temp_list = []

n = 
s = 
e = 
w = 

if i == 0 and j == 0:
    temp_list.append(locations[i + 1][j])
    temp_list.append(locations[i][j + 1])
