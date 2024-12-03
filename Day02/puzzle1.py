#!/usr/bin/env python3

# Define the required functions
def check_increasing(input_list):
    """
    This function checks if a list is strickly increasing.
    input_list: This is a list of integers 
    output: True if the list is strickly increasing, false otherwise."""
    temp = input_list[0]
    for ind in range(1, len(input_list)):
        if temp < input_list[ind]:
            temp = input_list[ind]
        else:
            return False
    return True

def check_decreasing(input_list):
    """
    This function checks if a list is strickly decreasing.
    input_list: This is a list of integers 
    output: True if the list is strickly decreasing, false otherwise."""
    temp = input_list[0]
    for ind in range(1, len(input_list)):
        if temp > input_list[ind]:
            temp = input_list[ind]
        else:
            return False
    return True

def check_deltas(input_list):
    """
    This function checks if the deltas between the numbers are between 1 and 3 inclusive.
    input_list: This is a list of integers
    output: True if the delta between each integer is between 1 and 3 inclusive and false otherwise."""
    temp = [abs(x-y) for x, y in zip(input_list[:-1], input_list[1:])]
    if (min(temp) >= 1) & (max(temp) <= 3):
        return True
    else:
        return False

# Define the required variables
cnt = 0

# Open file and put data into lists
with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split(' ')
        line = [int(i) for i in line]
        if (check_increasing(line) | check_decreasing(line)) & check_deltas(line):
            cnt += 1
    
    # Print the output
    print(f"There are {cnt} safe reports.")
