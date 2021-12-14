count = 0

with open ('input.txt', 'r') as f:
    lines = f.readlines()

for i in range(len(lines) - 1):
    if int(lines[i+1]) - int(lines[i]) > 0:
        count = count + 1

print(count)