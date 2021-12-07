# Read input
from typing import Counter


with open("input.txt", "r") as f:
    l = f.readline()


# Parse input
positions = list(map(int, l.split(",")))


fuel_cost = [0 for _ in range(max(positions))]

for new_pos in range(min(positions), max(positions)):
    for position in positions:
        horizontal_steps = abs(position - new_pos)
        crab_fuel_cost = 0
        while horizontal_steps > 0:
            crab_fuel_cost = crab_fuel_cost + horizontal_steps
            horizontal_steps = horizontal_steps - 1
        fuel_cost[new_pos] = fuel_cost[new_pos] + crab_fuel_cost

print(min(fuel_cost))