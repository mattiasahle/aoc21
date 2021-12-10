# Read input
with open("input.txt", "r") as f:
    lines = f.readlines()


openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']
scores = []


for line in lines:
    line_openers = ''
    is_corrupt = False
    completing_string = ''

    for char in line:
        if char in openers:
            line_openers = line_openers + char
        elif char in closers:
            if openers.index(line_openers[-1]) == closers.index(char):
                line_openers = line_openers[:-1]
            else:
                is_corrupt = True

    if is_corrupt:
        continue
    else:
        for char in reversed(line_openers):
            completing_string = completing_string + closers[openers.index(char)]

        score = 0
        for char in completing_string:
            if char == ')': point = 1
            elif char == ']': point = 2
            elif char == '}': point = 3
            elif char == '>': point = 4
            score = score * 5 + point
        scores.append(score)


print(sorted(scores)[len(scores) // 2])