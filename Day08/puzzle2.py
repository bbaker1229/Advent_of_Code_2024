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
        possible_nodes = []
        for check_ind in range(item_ind+1, len(locations)):
            next_item = locations[check_ind]
            vert_change = (item[0] - next_item[0])
            horz_change = (item[1] - next_item[1])
            for i in range(len(world_map)+1):
                node1 = (item[0] + i*vert_change, item[1] + i*horz_change)
                node2 = (item[0] - i*vert_change, item[1] - i*horz_change)
                possible_nodes.append(node1)
                possible_nodes.append(node2)
            for node in set(possible_nodes):
                if (node[0] >= 0) and (node[0] < len(world_map)):
                    if (node[1] >= 0) and (node[1] < len(world_map[0])):
                        node_dict[node] = 1

# Print the result
print(f"The number of unique anti-nodes is: {len(set(node_dict.keys()))}")
