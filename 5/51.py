with open("input.txt", "r") as f:
    lines = f.readlines()

coordinates = []

for line in lines:
    line.replace("\n", "")
    coordinates.append(line.replace('\n', '').split(' -> '))
    
for line in coordinates:
    
