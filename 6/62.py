with open("input.txt", "r") as f:
    fishes = f.readline()

# Create draw list of integers
fishes = list(map(int, fishes.replace("\n", "").split(",")))
fishes = [3,4,3,1,2]
fish_count = 0

for day in range(80):
    for fish in range(len(fishes)):
        while fishes[fish] % day > 7:
            fish_count = fish_count + 

print(fishes)
