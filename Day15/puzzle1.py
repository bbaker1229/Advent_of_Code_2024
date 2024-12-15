#!/usr/bin/env python3

# Create the required functions
def printMap(world_map):
    for row in world_map:
        print("".join(row))

def locateRobot(world_map):
    for row in range(len(world_map)):
        for col in range(len(world_map[0])):
            if world_map[row][col] == '@':
                return [row, col]
    return [-1, -1]

def updateMap(action, world_map):
    robot_location = locateRobot(world_map)
    row = robot_location[0]
    col = robot_location[1]
    if action == '^':
        while (world_map[row-1][col] == 'O') and (world_map[row-1][col] != '#'):
            row -= 1
        while (row != robot_location[0]) and (world_map[row-1][col] != '#'):
            temp = world_map[row][col]
            world_map[row][col] = world_map[row-1][col]
            world_map[row-1][col] = temp
            row += 1
        if world_map[row-1][col] == '.':
            temp = world_map[row][col]
            world_map[row][col] = world_map[row-1][col]
            world_map[row-1][col] = temp
    if action == '>':
        while (world_map[row][col+1] == 'O') and (world_map[row][col+1] != '#'):
            col += 1
        while (col != robot_location[1]) and (world_map[row][col+1] != '#'):
            temp = world_map[row][col]
            world_map[row][col] = world_map[row][col+1]
            world_map[row][col+1] = temp
            col -= 1
        if world_map[row][col+1] == '.':
            temp = world_map[row][col]
            world_map[row][col] = world_map[row][col+1]
            world_map[row][col+1] = temp
    if action == 'v':
        while (world_map[row+1][col] == 'O') and (world_map[row+1][col] != '#'):
            row += 1
        while (row != robot_location[0]) and (world_map[row+1][col] != '#'):
            temp = world_map[row][col]
            world_map[row][col] = world_map[row+1][col]
            world_map[row+1][col] = temp
            row -= 1
        if world_map[row+1][col] == '.':
            temp = world_map[row][col]
            world_map[row][col] = world_map[row+1][col]
            world_map[row+1][col] = temp
    if action == '<':
        while (world_map[row][col-1] == 'O') and (world_map[row][col-1] != '#'):
            col -= 1
        while (col != robot_location[1]) and (world_map[row][col-1] != '#'):
            temp = world_map[row][col]
            world_map[row][col] = world_map[row][col-1]
            world_map[row][col-1] = temp
            col += 1
        if world_map[row][col-1] == '.':
            temp = world_map[row][col]
            world_map[row][col] = world_map[row][col-1]
            world_map[row][col-1] = temp

def applyGPS(world_map):
    total = 0
    for row in range(len(world_map)):
        for col in range(len(world_map[0])):
            if world_map[row][col] == 'O':
                total += (100 * row + col)
    return total

# Create the required variables
world_map = []
movements = []

# Read input file
with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        if '#' in line:
            line = list(line.strip())
            world_map.append(line)
        if ('<' in line) or ('^' in line) or ('>' in line) or ('v' in line):
            movements += list(line.strip())

while movements:
    action = movements.pop(0)
    updateMap(action, world_map)
    # printMap(world_map)

total = applyGPS(world_map)

print(f"The total is: {total}")
