# Task
# Part 1 = 80 days
# Part 2 = 256 days
DAYS = 80

# Read input
with open("input.txt", "r") as f:
    fishes = f.readline()

# Parse input to list of integers
fishes = list(map(int, fishes.replace("\n", "").split(",")))


for day in range(DAYS):
    for fish in range(len(fishes)):
        if fishes[fish] == 0:
            fishes.append(8)    # Array fills memory in task 2
            fishes[fish] = 6
        else:
            fishes[fish] = fishes[fish] - 1


print(len(fishes))
