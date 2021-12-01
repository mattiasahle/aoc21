count = 1

with open('input.txt', 'r') as f:
    lines = f.readlines()

prev_sum = int(lines[0]) + int(lines[1]) + int(lines[2])
sum = int(lines[1]) + int(lines[2]) + int(lines[3])

for i in range(3,len(lines) - 1):
    prev_sum = prev_sum + int(lines[i]) - int(lines[i-3])
    sum = sum + int(lines[i+1]) - int(lines[i-2])

    print(i)
    print('prev:\t', prev_sum)
    print('sum:\t', sum)
    print()
    
    if sum > prev_sum:
        count = count + 1

print(count)