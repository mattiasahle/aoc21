count = 1

with open('input.txt', 'r') as f:
    lines = list(map(int, f.readlines()))

prev_sum = lines[0] + lines[1] + lines[2]
sum = lines[1] + lines[2] + lines[3]

for i in range(3, len(lines) - 1):
    prev_sum = prev_sum + lines[i] - lines[i-3]
    sum = sum + lines[i+1] - lines[i-2]

    if sum > prev_sum:
        count = count + 1

print(count)