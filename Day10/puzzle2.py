#!/usr/bin/env python3
from collections import defaultdict

# Create the required functions
def actions(trail_map, current_location):
    current_row = current_location[0]
    current_col = current_location[1]
    current_trail_value = trail_map[current_row][current_col]
    target_trail_value = str(int(current_trail_value)+1)
    possible_actions = []
    # check up
    if (current_row-1 >= 0) and (trail_map[current_row-1][current_col] == target_trail_value):
        possible_actions.append((current_row-1, current_col))
    # check right
    if (current_col+1 < len(trail_map[0])) and (trail_map[current_row][current_col+1] == target_trail_value):
        possible_actions.append((current_row, current_col+1))
    # check down
    if (current_row+1 < len(trail_map)) and (trail_map[current_row+1][current_col] == target_trail_value):
        possible_actions.append((current_row+1, current_col))
    # check left
    if (current_col-1 >= 0) and (trail_map[current_row][current_col-1] == target_trail_value):
        possible_actions.append((current_row, current_col-1))
    return possible_actions

def find_trail_rating(trail_map, start_location):
    trail_ends_dict = defaultdict(int)
    current_location = start_location
    horizon = []
    horizon.append(current_location)
    while len(horizon) > 0:
        current_location = horizon.pop()
        if trail_map[current_location[0]][current_location[1]] == '9':
            trail_ends_dict[current_location] += 1
        possible_actions = actions(trail_map, current_location)
        for act in possible_actions:
            horizon.append(act)
    cnt = 0
    for location in trail_ends_dict.keys():
        cnt += trail_ends_dict[location]
    return cnt

trail_map = []

# Read map
with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        trail_map.append(list(line.strip()))

# Find all trailheads
trailheads = []
for row in range(len(trail_map)):
    for col in range(len(trail_map[0])):
        if trail_map[row][col] == '0':
            trailheads.append((row, col))

# Find the count of all trails
total_cnt = 0
for item in trailheads:
    cnt = find_trail_rating(trail_map, item)
    total_cnt += cnt

# print the total count
print(f"The total trail rating is: {total_cnt}")