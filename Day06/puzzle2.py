#!/usr/bin/env python3
import os
from collections import defaultdict

# Create required functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_position(world_map):
    for i in range(len(world_map)):
        for j in range(len(world_map[0])):
            if (world_map[i][j] == '^') or (world_map[i][j] == '>') or (world_map[i][j] == '<') or (world_map[i][j] == 'v'):
                return (i, j, world_map[i][j])

def action(world_map):
    current_x, current_y, direction = find_position(world_map)
    if direction == '^':
        if (current_x-1 >= 0) and (world_map[current_x-1][current_y] == '#'):
            return (current_x, current_y, '>')
        else:
            return (current_x-1, current_y, '^')
    if direction == '>':
        if (current_y+1 < len(world_map[0])) and (world_map[current_x][current_y+1] == '#'):
            return (current_x, current_y, 'v')
        else:
            return (current_x, current_y+1, '>')
    if direction == 'v':
        if (current_x+1 < len(world_map)) and (world_map[current_x+1][current_y] == '#'):
            return (current_x, current_y, '<')
        else:
            return (current_x+1, current_y, 'v')
    if direction == '<':
        if (current_y-1 >= 0) and (world_map[current_x][current_y-1] == '#'):
            return (current_x, current_y, '^')
        else:
            return (current_x, current_y-1, '<')

def update_map(world_map, move):
    next_x, next_y, direction = move
    current_x, current_y, _ = find_position(world_map)
    world_map[current_x][current_y] = '.'
    world_map[next_x][next_y] = direction
    return world_map

def print_local_map(world_map):
    clear_screen()
    current_x, current_y, _ = find_position(world_map)
    if current_x-10 < 0:
        low_x = 0
    else:
        low_x = current_x-10
    if current_x+10 >= len(world_map):
        high_x = len(world_map)
    else:
        high_x = current_x+10
    if current_y-10 < 0:
        low_y = 0
    else:
        low_y = current_y-10
    if current_y+10 >= len(world_map[0]):
        high_y = len(world_map[0])
    else:
        high_y = current_y+10
    print(f"Current position: {(current_x, current_y)}")
    for line in world_map[low_x:high_x]:
        print(''.join(line[low_y:high_y]))

# Create variables
world_map = []
position_dict = {}
loop_counter = 0
cnt = 1

# Read map
# with open("E:/Github/Advent_of_Code_2024/Day06/input.txt", 'r', encoding='utf-8') as f:
with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        world_map.append(list(line.strip()))

# print(f"There are {len(world_map)} rows.")
# print(f"There are {len(world_map[0])} columns.")

# Find the unique locations
current_x, current_y, _ = find_position(world_map)
position_dict[(current_x, current_y)] = 1
new_world = []
for line in world_map:
    new_world.append(line[:])
next_move = action(new_world)
while (0 <= next_move[0] < len(new_world)) and (0 <= next_move[1] < len(new_world[0])):
    position_dict[(next_move[0], next_move[1])] = 1
    new_world = update_map(new_world, next_move)
    # print_local_map(new_world)
    # input("Press enter to continue...")
    next_move = action(new_world)

# check if adding an obstruction causes a loop
for item in position_dict.keys():
    loop_dict = defaultdict(int)
    print(f"checking item {cnt} of {len(position_dict.keys())}")
    if world_map[item[0]][item[1]] == '^':
        cnt += 1
        continue
    new_world = []
    for line in world_map:
        new_world.append(line[:])
    new_world[item[0]][item[1]] = '#'
    current_x, current_y, _ = find_position(new_world)
    loop_dict[(current_x, current_y)] = 1
    next_move = action(new_world)
    while (0 <= next_move[0] < len(new_world)) and (0 <= next_move[1] < len(new_world[0])):
        loop_dict[(next_move[0], next_move[1])] += 1
        if loop_dict[(next_move[0], next_move[1])] > 8:
            loop_counter += 1
            print(loop_counter)
            break
        new_world = update_map(new_world, next_move)
        # print_local_map(new_world)
        # input("Press enter to continue...")
        next_move = action(new_world)
    cnt += 1

# print the number of unique locations
print(f"The number of unique locations is: {loop_counter}")
