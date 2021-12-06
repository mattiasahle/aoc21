with open("input.txt", "r") as f:
    fishes = f.readline()

# Create draw list of integers
fishes = list(map(int, fishes.replace("\n", "").split(",")))

for day in range(80):
    for fish in range(len(fishes)):
        if fishes[fish] == 0:
            fishes.append(8)
            fishes[fish] = 6
        else:
            fishes[fish] = fishes[fish] - 1

print(len(fishes))
