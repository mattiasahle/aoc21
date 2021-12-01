count = 1

with open('input.txt', 'r') as f:
    lines = list(map(int, f.readlines()))

prev_sum = sum(lines[0:3])

for i in range(3, len(lines)-1):
    new_sum = sum(lines[i-2:i+1])

    if new_sum > prev_sum:
        count = count + 1

    prev_sum = new_sum
    new_sum = 0

print(count)