# Task
# Part 1 = 80 days
# Part 2 = 256 days
DAYS = 4

# Read input
with open("input.txt", "r") as f:
    fishes = f.readline()

# Parse input to list of  integers
# fishes = list(map(int, fishes.replace("\n", "").split(",")))
fishes = [3, 4, 3, 1, 2]


fish_count = len(fishes)


for fish in fishes:
    for countdown in range(DAYS - 1, -1, -1):
        fish_spawns = countdown // (fish % 7)
        print(fish_spawns)
        fish_count = fish_count + fish_spawns
        

print(fish_count)