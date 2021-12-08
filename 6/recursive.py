# Task
# Part 1 = 80 days
# Part 2 = 256 days
DAYS = 80

# Read input
with open("input.txt", "r") as f:
    fishes = f.readline()

# Parse input to list of integers
fishes = list(map(int, fishes.replace("\n", "").split(",")))


fish_count = len(fishes)


def count_fish(fish, days):
    fish_count = 0

    while days > 0:
        days = days - 1
        fish = fish - 1

        if fish < 0:
            fish = 6
            fish_count = fish_count + 1
            fish_count = fish_count + count_fish(8, days)

    return fish_count


for fish in fishes:
    fish_count = fish_count + count_fish(fish, DAYS)


print(fish_count)
