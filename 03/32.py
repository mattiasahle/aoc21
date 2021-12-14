with open("input.txt", "r") as f:
    input = f.readlines()

oxygen = input.copy()
co2 = input.copy()


def count_bits(numbers, bit):
    zeros = 0
    ones = 0

    for number in numbers:
        if number[bit] == "0":
            zeros = zeros + 1
        if number[bit] == "1":
            ones = ones + 1

    return zeros, ones


def remove_numbers(numbers, value, bit):
    finished = False

    while not finished:
        finished = True

        for number in numbers:
            if number[bit] == value:
                numbers.remove(number)
                finished = False


for bit in range(12):
    if len(oxygen) > 1:
        zeros, ones = count_bits(oxygen, bit)

        if zeros > ones:
            remove_numbers(oxygen, "1", bit)
        elif zeros < ones:
            remove_numbers(oxygen, "0", bit)
        elif zeros == ones:
            remove_numbers(oxygen, "0", bit)


for bit in range(12):
    if len(co2) > 1:
        zeros, ones = count_bits(co2, bit)

        if zeros > ones:
            remove_numbers(co2, "0", bit)
        elif zeros < ones:
            remove_numbers(co2, "1", bit)
        elif zeros == ones:
            remove_numbers(co2, "1", bit)


print(int(oxygen[-1], 2) * int(co2[-1], 2))
