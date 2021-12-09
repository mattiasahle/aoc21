line = [['dacefg', 'fegab', 'de', 'dceb', 'bedag', 'dae', 'bcgaefd', 'bdacg', 'fbgcad', 'bgedca'], ['acfebgd', 'de', 'dbagc', 'deagcb']]
decoded_line = [[None, None, 1, 4, None, 7, 8, None, None, None], [8, 1, None, None]]
segments = ['a', '', 'de', '', '', 'de', '']

three = ''

for number in line[0]:
    if len(number) == 5:
        if segments[2][0] in number and segments[2][1] in number:
            three = number

for i in range(len(line)):
    for j in range(len(line[i])):
        if line[i][j] == three:
            decoded_line[i][j] = 3

print(line)
print(decoded_line)