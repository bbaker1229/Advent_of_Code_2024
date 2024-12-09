#!/usr/bin/env python3
from collections import defaultdict

# Create variables
world_map = []
antenna_dict = defaultdict(list)
node_dict = defaultdict(int)

# Read map
with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        world_map.append(list(line.strip()))

# print(world_map)

# Find all of the antenna types and their locations
for row_ind in range(len(world_map)):
    for col_ind in range(len(world_map[0])):
        item = world_map[row_ind][col_ind]
        if item != '.':
            antenna_dict[item] = antenna_dict[item] + [(row_ind, col_ind)]

# print(antenna_dict)

# Find the locations of all the anti-nodes
for _, (ant_type, locations) in enumerate(antenna_dict.items()):
    # print(f"{ant_type}: {locations}")
    for item_ind in range(len(locations)-1):
        item = locations[item_ind]
        for check_ind in range(item_ind+1, len(locations)):
            next_item = locations[check_ind]
            vert_change = (item[0] - next_item[0])
            horz_change = (item[1] - next_item[1])
            first_node = (item[0] + vert_change, item[1] + horz_change)
            second_node = (next_item[0] - vert_change, next_item[1] - horz_change)
            # print(f"ant_type: {ant_type}; ant_1: {item}; ant_2: {next_item}; first_node: {first_node}; second_node: {second_node}")
            if (first_node[0] >= 0) and (first_node[0] < len(world_map)):
                if (first_node[1] >= 0) and (first_node[1] < len(world_map[0])):
                    node_dict[first_node] = 1
            if (second_node[0] >= 0) and (second_node[0] < len(world_map)):
                if (second_node[1] >= 0) and (second_node[1] < len(world_map[0])):
                    node_dict[second_node] = 1

# Print the result
print(f"The number of unique anti-nodes is: {len(set(node_dict.keys()))}")
