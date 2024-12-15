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

def createMap(robot_dict):
    robot_map = []
    for i in range(N_ROWS):
        row = []
        for j in range(N_COLS):
            row.append('.')
        robot_map.append(row)
    for robot in robot_dict.keys():
        position = robot_dict[robot]['position']
        robot_map[position[1]][position[0]] = 'X'
    return robot_map

def printMap(robot_map):
    for row in robot_map:
        print("".join(row))

def possibleMatch(robot_map):
    for row in range(len(robot_map)):
        line = robot_map[row]
        cnt = 0
        for col in range(len(line)-1):
            if (line[col] == line[col+1]) and (line[col] == 'X'):
                cnt += 1
                if cnt > 15:
                    return True
            else:
                cnt = 0
    return False 

# Create required variables
robot_dict = {}
cnt = 0
N_ROWS = 103
N_COLS = 101

# Read input file
with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split(' ')
        position = line[0][2:].split(',')
        position = [int(i) for i in position]
        velocity = line[1][2:].split(',')
        velocity = [int(i) for i in velocity]
        robot_dict[cnt] = {'position': position, 'velocity': velocity}
        cnt += 1

# Tick through time
for i in range(10000):
    tick(robot_dict)
    robot_map = createMap(robot_dict)
    if possibleMatch(robot_map):
        printMap(robot_map)
        print(f"seconds: {i+1}")
