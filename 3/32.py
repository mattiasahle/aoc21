with open("input.txt", "r") as f:
    input = f.readlines()

def count_bits(lines):
    zeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for line in lines:
        for i in range(len(line)):
            if line[i] == "0":
                zeros[i] = zeros[i] + 1
            if line[i] == "1":
                ones[i] = ones[i] + 1

    return zeros, ones


oxygen = input
zeros, ones = count_bits(oxygen)

while len(oxygen) > 1:
    for i in range(len(zeros)):
        zeros, ones = count_bits(oxygen)

        if len(oxygen) == 1:
            break

        # print(oxygen)
        # print(zeros[i])
        # print(ones[i])
        # print('bit pos: ', i)

        finished = False

        while not finished:
            finished = True

            for line in oxygen:
                if len(oxygen) == 1:
                    break
                if zeros[i] > ones[i] and line[i] == '1':
                    print('removed', line)
                    oxygen.remove(line)
                    finished = False
                elif zeros[i] < ones[i] and line[i] == '0':
                    print('removed', line)
                    oxygen.remove(line)
                    finished = False
                elif zeros[i] == ones[i] and line[i] == '0':
                    print('removed', line)
                    oxygen.remove(line)
                    finished = False

print(oxygen)


co2 = input
zeros, ones = count_bits(co2)

while len(co2) > 1:
    for i in range(len(zeros)):
        zeros, ones = count_bits(co2)

        if len(co2) == 1:
            break

        # print(co2)
        # print(zeros[i])
        # print(ones[i])
        # print('bit pos: ', i)

        finished = False

        while not finished:
            finished = True

            for line in co2:
                if len(co2) == 1:
                    break
                if zeros[i] > ones[i] and line[i] == '0':
                    print('removed', line)
                    co2.remove(line)
                    finished = False
                elif zeros[i] < ones[i] and line[i] == '1':
                    print('removed', line)
                    co2.remove(line)
                    finished = False
                elif zeros[i] == ones[i] and line[i] == '1':
                    print('removed', line)
                    co2.remove(line)
                    finished = False

print(co2)


print(int(oxygen[-1], 2) * int(co2[-1], 2))
