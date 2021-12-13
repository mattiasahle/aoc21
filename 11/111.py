# Read input
with open("input.txt", "r") as f:
    l = f.readlines()


# Parse input
l = [i.replace("\n", "") for i in l]
octopuses = [list(map(int, [c for c in line])) for line in l]


# Functions
def print_octopuses():
    print()
    for i in octopuses:
        print(i)


# Tested
def increment_energy_levels():
    for i in range(len(octopuses)):
        for j in range(len(octopuses[i])):
            octopuses[i][j] = octopuses[i][j] + 1


# Tested
def get_incrementers(i, j):
    incrementers = []
    
    if i + 1 < 10: incrementers.append([i + 1, j])
    if i + 1 < 10 and j - 1 >= 0: incrementers.append([i + 1, j - 1])
    if j - 1 >= 0: incrementers.append([i, j - 1])
    if i - 1 >= 0 and j - 1 >= 0: incrementers.append([i - 1, j - 1])
    if i - 1 >= 0: incrementers.append([i - 1, j])
    if i - 1 >= 0 and j + 1 < 10: incrementers.append([i - 1, j + 1])
    if j + 1 < 10: incrementers.append([i, j + 1])
    if i + 1 < 10 and j + 1 < 10: incrementers.append([i + 1, j + 1])

    return incrementers


# Tested
def increment_adjacent(i ,j):
    incrementers = get_incrementers(i, j)

    for octopus in incrementers:
        octopuses[octopus[0]][octopus[1]] = octopuses[octopus[0]][octopus[1]] + 1


def flash_flash_surrounded_octopuses():
    number_of_flashes = 0

    for i in range(len(octopuses)):
        for j in range(len(octopuses[i])):
            number_of_surrounding_flashers = 0

            if i + 1 < 10: 
                if octopuses[i + 1][j] == 0: number_of_surrounding_flashers = number_of_surrounding_flashers + 1
            if i + 1 < 10 and j - 1 >= 0:
                if octopuses[i + 1][j - 1] == 0: number_of_surrounding_flashers = number_of_surrounding_flashers + 1
            if j - 1 >= 0:
                if octopuses[i][j - 1] == 0: number_of_surrounding_flashers = number_of_surrounding_flashers + 1
            if i - 1 >= 0 and j - 1 >= 0:
                if octopuses[i - 1][j - 1] == 0: number_of_surrounding_flashers = number_of_surrounding_flashers + 1
            if i - 1 >= 0:
                if octopuses[i - 1][j] == 0: number_of_surrounding_flashers = number_of_surrounding_flashers + 1
            if i - 1 >= 0 and j + 1 < 10:
                if octopuses[i - 1][j + 1] == 0: number_of_surrounding_flashers = number_of_surrounding_flashers + 1
            if j + 1 < 10:
                if octopuses[i][j + 1] == 0: number_of_surrounding_flashers = number_of_surrounding_flashers + 1
            if i + 1 < 10 and j + 1 < 10:
                if octopuses[i + 1][j + 1] == 0: number_of_surrounding_flashers = number_of_surrounding_flashers + 1

            if number_of_surrounding_flashers == 8:
                octopuses[i, j] = 0
                number_of_flashes = number_of_flashes + 1

    return number_of_flashes


def flash_flashers():
    has_flashed = True
    number_of_flashes = 0

    while has_flashed:
        has_flashed = False

        for i in range(len(octopuses)):
            for j in range(len(octopuses[i])):
                if octopuses[i][j] > 9:
                    octopuses[i][j] = 0
                    number_of_flashes = number_of_flashes + 1
                    has_flashed = True
                    increment_adjacent(i, j)

        number_of_flashes = number_of_flashes + flash_flash_surrounded_octopuses()

    return number_of_flashes


# Main
number_of_flashes = 0

for _ in range(100):
    increment_energy_levels()
    number_of_flashes = number_of_flashes + flash_flashers()

print(number_of_flashes)
# Too high: 2964