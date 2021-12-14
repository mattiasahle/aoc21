horizontal = 0
depth = 0

with open("input.txt", "r") as f:
    lines = f.readlines()
    
# print(type(int(lines[0][-2])))

for i in range(len(lines)):
    value = [int(s) for s in lines[i].split() if s.isdigit()]

    if 'forward' in lines[i]:
        horizontal = horizontal + value[0]
    if 'down' in lines[i]:
        depth = depth + value[0]
    if 'up' in lines[i]:
        depth = depth - value[0]

print(horizontal)
print(depth)
print(horizontal * depth)