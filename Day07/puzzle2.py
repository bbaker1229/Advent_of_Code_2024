#!/usr/bin/env python3
from itertools import product

# Define required variables
total = 0

# Read input file
# with open("test_input.txt", 'r', encoding='utf-8') as f:
with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split(':')
        test_value = int(line[0])
        line = line[1]
        line = line.strip().split(' ')
        line = [int(i) for i in line]
        operator_slots = len(line) - 1
        continue_flag = 1
        if continue_flag:
            combos = [list(comb) for comb in product(['+', '*'], repeat=operator_slots)]
            for item in combos:
                temp_value = line[0]
                for i in range(len(item)):
                    operator = item[i]
                    if operator == '+':
                        temp_value += line[i+1]
                    if operator == '*':
                        temp_value *= line[i+1]
                if temp_value == test_value:
                    total += test_value
                    continue_flag = 0
                    break
        if continue_flag:
            combos = [list(comb) for comb in product(['+', '*', '||'], repeat=operator_slots)]
            for item in combos:
                temp_value = line[0]
                for i in range(len(item)):
                    operator = item[i]
                    if operator == '+':
                        temp_value += line[i+1]
                    if operator == '*':
                        temp_value *= line[i+1]
                    if operator == '||':
                        num_digits = len(str(line[i+1]))
                        temp_value *= pow(10, num_digits)
                        temp_value += line[i+1]
                if temp_value == test_value:
                    total += test_value
                    continue_flag = 0
                    break

# print the result
print(f"The total is: {total}")