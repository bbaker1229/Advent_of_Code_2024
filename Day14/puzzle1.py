#!/usr/bin/env python3

# Create the required functions
def tick(robot_dict):
    for robot in robot_dict.keys():
        position = robot_dict[robot]['position']
        velocity = robot_dict[robot]['velocity']
        # new column:
        position[0] = (position[0] + velocity[0]) % N_COLS
        # new row:
        position[1] = (position[1] + velocity[1]) % N_ROWS
        robot_dict[robot]['position'] = position

def countQuads(robot_dict):
    skip_row = (N_ROWS - 1) // 2
    skip_col = (N_COLS - 1) // 2
    quads = [0,0,0,0]
    for robot in robot_dict.keys():
        position = robot_dict[robot]['position']
        if (position[0] < skip_col) and (position[1] < skip_row): # top left quad
            quads[0] += 1
        if (position[0] > skip_col) and (position[1] < skip_row): # top right quad
            quads[1] += 1
        if (position[0] < skip_col) and (position[1] > skip_row): # bottom left quad
            quads[2] += 1
        if (position[0] > skip_col) and (position[1] > skip_row): # bottom right quad
            quads[3] += 1
    return quads

# Create required variables
robot_dict = {}
cnt = 0
N_ROWS = 103
N_COLS = 101

# Read input file
# with open("E:/Github/Advent_of_Code_2024/Day14/test_input.txt", 'r', encoding='utf-8') as f:
with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split(' ')
        position = line[0][2:].split(',')
        position = [int(i) for i in position]
        velocity = line[1][2:].split(',')
        velocity = [int(i) for i in velocity]
        robot_dict[cnt] = {'position': position, 'velocity': velocity}
        cnt += 1

# print(robot_dict)

# Tick through time
for i in range(100):
    tick(robot_dict)

# Get the counts in each quad
counts = countQuads(robot_dict)

# Calculate the safety factor
total = 1
for i in counts:
    total *= i

# Print the results.
print(f"The safety factor is: {total}")
