# Read input
with open("input.txt", "r") as f:
    l = f.readline()


# Parse input
positions = list(map(int, l.split(",")))


fuel_cost = [0 for _ in range(max(positions))]

for new_pos in range(min(positions), max(positions)):
    for position in positions:
        fuel_cost[new_pos] = fuel_cost[new_pos] + abs(position - new_pos)

print(min(fuel_cost))