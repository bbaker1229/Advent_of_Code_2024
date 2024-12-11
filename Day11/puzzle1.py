#!/usr/bin/env python3

# Define required functions
def flatten_list(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

def apply_rules(item):
    if item == 0:
        return [1]
    elif len(str(item)) % 2 == 0:
        return [item//pow(10,len(str(item))//2), item%pow(10,len(str(item))//2)]
    else:
        return [item * 2024]
    
def blink(stones):
    new_list = []
    for stone in stones:
        new_list.append(apply_rules(stone))
    return flatten_list(new_list)

# Read input file
with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        stones = line.strip().split(' ')
stones = [int(i) for i in stones]

# Blink
for i in range(25):
    stones = blink(stones)
    # print(stones)

# Print the results
print(f"There are {len(stones)} stones after 25 blinks.")
