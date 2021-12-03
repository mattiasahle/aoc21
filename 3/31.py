with open("input.txt", "r") as f:
    lines = f.readlines()

zeros = [0,0,0,0,0,0,0,0,0,0,0,0]
ones = [0,0,0,0,0,0,0,0,0,0,0,0]
epsilon = ""
gamma = ""

for line in lines:
    for i in range(len(line)):
        if line[i] == '0':
            zeros[i] = zeros[i] + 1
        if line[i] == '1':
            ones[i] = ones[i] + 1

for i in range(len(zeros)):
    if zeros[i] > ones[i]:
        epsilon = epsilon + "1"
        gamma = gamma + "0"
    else:
        epsilon = epsilon + "0"
        gamma = gamma + "1"

print(int(epsilon,2)*int(gamma,2))
    