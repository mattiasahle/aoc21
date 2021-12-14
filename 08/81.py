# Read input
with open("input.txt", "r") as f:
    l = f.readlines()

# Parse input
output_values = list(i.split(' | ') for i in l)
output_values = [o[1].replace('\n', '') for o in output_values]
output_values = list(o.split(' ') for o in output_values)

unique_numbers = [2, 3, 4, 7]
count = 0

for i in output_values:
    for j in i:
        for number in unique_numbers:
            if len(j) == number:
                count = count + 1


print(count)