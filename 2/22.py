horizontal = 0
depth = 0
aim = 0

with open("input.txt", "r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    value = [int(s) for s in lines[i].split() if s.isdigit()]

    if "down" in lines[i]:
        aim = aim + value[0]
    if "up" in lines[i]:
        aim = aim - value[0]
    if "forward" in lines[i]:
        horizontal = horizontal + value[0]
        depth = depth + aim * value[0]

print(aim)
print(horizontal)
print(depth)
print(horizontal * depth)
