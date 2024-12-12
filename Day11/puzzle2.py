#!/usr/bin/env python3
from collections import defaultdict

stone_dict = defaultdict(int)

# Define required functions
def apply_rules(item):
    if item == 0:
        return [1]
    elif len(str(item)) % 2 == 0:
        return [item//pow(10,len(str(item))//2), item%pow(10,len(str(item))//2)]
    else:
        return [item * 2024]
    
def blink(stones):
    new_dict = defaultdict(int)
    for stone in stones.keys():
        cnt = stones[stone]
        new_stones = apply_rules(stone)
        for item in new_stones:
            new_dict[item] = (new_dict[item] + cnt)
    return new_dict

# Read input file
with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        stones = line.strip().split(' ')
stones = [int(i) for i in stones]

# Add to dictionary
for stone in stones:
    stone_dict[stone] = 1

# Blink
for i in range(75):
    stone_dict = blink(stone_dict)

# Print the results
total = 0
for stone in stone_dict.keys():
    total += stone_dict[stone]

print(f"There are {total} stones after 75 blinks.")
