#!/usr/bin/env python3
from collections import defaultdict

# Create required functions
def pass_page_rules(line, my_dict):
    for check_ind in range(len(line)-1, 0, -1):
        value = line[check_ind]
        temp_lst = my_dict[value]
        ind = 0
        if len(temp_lst) > 0:
            while ind < check_ind:
                if line[ind] in temp_lst:
                    return False
                ind += 1
    return True

# Create required variables
my_dict = defaultdict(list)
total = 0

# Open file and put data into lists
with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        if '|' in line:
            # add info for first of file
            line = line.split('|')
            line = [int(i) for i in line]
            current_list = my_dict[line[0]]
            if len(current_list) == 0:
                my_dict[line[0]] = [line[1]]
            else:
                my_dict[line[0]] = current_list + [line[1]]
        if ',' in line:
            # add info for second of file
            line = line.split(',')
            line = [int(i) for i in line]
            if pass_page_rules(line, my_dict):
                total += line[len(line)//2]

# Print the result
print(f"The total is: {total}")
