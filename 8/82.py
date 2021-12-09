# Read input
with open("input.txt", "r") as f:
    lines = f.readlines()

# Parse input
lines = [i.split(' | ') for i in lines]
lines = [[i[0], i[1].replace('\n', '')] for i in lines]
lines = [[j.split(' ') for j in i] for i in lines]

for line in lines[0:10]:
    print(line)
print()


# Variables
EIGHT = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
UNIQUE_NUMBERS = [(2, 1), (3, 7), (4, 4), (7, 8)]   # (Segments, Number)
result = 0


# Functions
def decode_unique_numbers(line):
    decoded_line = [[None for _ in range(len(line[0]))], [None for _ in range(len(line[1]))]]

    for i in range(len(line)):
        for j in range(len(line[i])):
            for k in range(len(UNIQUE_NUMBERS)):
                if len(line[i][j]) == UNIQUE_NUMBERS[k][0]:
                    decoded_line[i][j] = UNIQUE_NUMBERS[k][1]
    
    print('Unique:\t', decoded_line)
    return decoded_line


# Find letter for segment 0 using numbers 7 and 1
# Bonus: Narrow in on two numbers for segments 2 and 5
def decode_segment_0(line, decoded_line):
    seven = ''
    one = ''

    for i in range(len(decoded_line[0])):
        if decoded_line[0][i] == 7:
            seven = line[0][i]
        if decoded_line[0][i] == 1:
            one = line[0][i]

    for c in seven:
        if c not in one:
            segments[0] = c
        else:
            segments[2] = segments[2] + c
            segments[5] = segments[5] + c

    print('Seg 0:\t', segments)


def decode_number_3(line, decoded_line):
    three = ''

    for number in line[0]:
        if len(number) == 5:
            if segments[2][0] in number and segments[2][1] in number:
                three = number

    for i in range(len(line)):
        for j in range(len(line[i])):
            if line[i][j] == three:
                decoded_line[i][j] = 3

    print('Three:\t', decoded_line)


# Not working correctly
def decode_segment_1(line, decoded_line):
    three = ''
    four = ''

    for i in range(len(decoded_line[0])):
        if decoded_line[0][i] == 3:
            three = line[0][i]
        if decoded_line[0][i] == 4:
            four = line[0][i]

    for c in three:
        if c not in four:
            segments[1] = c
        # else:
        #     segments[2] = segments[2] + c
        #     segments[5] = segments[5] + c

    print('Seg 1:\t', segments)


# Main
for line in lines[0:10]:
    segments = ['' for _ in range(7)]
    decoded_line = decode_unique_numbers(line)

    if None in decoded_line[1]:     # continue decoding
        decode_segment_0(line, decoded_line)
        decode_number_3(line, decoded_line)
            
        if None in decoded_line[1]:
            decode_segment_1(line, decoded_line) # Not working correctly


    # Summation after output values are decoded
    # result = result + sum(decoded_line[1])
    print()


# print(result)


# print(['bcgaefd' for _ in len(EIGHT)] in EIGHT)