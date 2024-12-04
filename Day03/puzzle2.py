#!/usr/bin/env python3
import re

# Create functions
def do_check(ind, do_lst, dont_lst):
    """
    This function returns True if the multiplication should be done and False otherwise.
    ind: This is the index of the multiplication item to check
    do_lst: This is a list of the indices for the "do" command.
    dont_lst: This is a list of the indices for the "dont" command.
    output: A boolean True to do multiplication and false otherwise.
    """
    do_ind = -1
    while (len(do_lst) > 0) and (do_lst[0] < ind):
        do_ind = do_lst.pop(0)
    dont_ind = -1
    while (len(dont_lst) > 0) and (dont_lst[0] < ind):
        dont_ind = dont_lst.pop(0)
    if do_ind > dont_ind:
        return True
    else:
        return False

# Create variables to use
pattern = r'mul\([0-9]{,3},[0-9]{,3}\)'
group_pattern = r'mul\(([0-9]{,3}),([0-9]{,3})\)'
do_pattern = r'do\(\)'
dont_pattern = r"don't\(\)"
total = 0
prev_flag = True

# Open file and put data into lists
with open("/home/bryan/src/Advent_of_Code_2024/Day03/input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        mul_locations = [(m.span()) for m in re.finditer(pattern, line)]
        do_locations = [int(m.start()) for m in re.finditer(do_pattern, line)]
        dont_locations = [int(m.start()) for m in re.finditer(dont_pattern, line)]
        if prev_flag:
            do_locations = [0] + do_locations
        else:
            dont_locations = [0] + dont_locations
        for item in mul_locations:
            # Check if we need to update the do and dont inds
            result = do_check(item[0], do_locations.copy(), dont_locations.copy())
            if result: # Do mult
                temp = line[item[0]:item[1]]
                match = re.search(group_pattern, temp)
                total += (int(match.group(1)) * int(match.group(2)))
        prev_flag = result

# Print the total result of the multiplications
print(f"The total is: {total}")
