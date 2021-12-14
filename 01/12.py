count = 0

with open("input.txt", "r") as f:
    lines = list(map(int, f.readlines()))

prev_sum = sum(lines[0:3])

for i in range(4, len(lines) + 1):
    new_sum = sum(lines[i - 3 : i])

    if new_sum > prev_sum:
        count = count + 1

    prev_sum = new_sum

print(count)
