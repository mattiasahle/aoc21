# Read input
with open("input.txt", "r") as f:
    lines = f.readlines()


openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']
illegal_chars = []
score = 0


for line in lines:
    line_openers = ''
    for char in line:
        if char in openers:
            line_openers = line_openers + char
        elif char in closers:
            if openers.index(line_openers[-1]) == closers.index(char):
                line_openers = line_openers[:-1]
            else:
                illegal_chars.append(char)
                break

for char in illegal_chars:
    if char == ')':
        score = score + 3
    elif char == ']':
        score = score + 57
    elif char == '}':
        score = score + 1197
    elif char == '>':
        score = score + 25137

print(score)