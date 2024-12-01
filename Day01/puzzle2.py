#!/usr/bin/env python3

from collections import Counter

# Define lists for use.
left_list = []
right_list = []
final_sum = 0

# Open file and put data into lists
with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split('  ')
        line[1] = line[1].strip()
        left_list.append(int(line[0]))
        right_list.append(int(line[1]))

# Count the number of unique items in the right list
right_list = Counter(right_list)

# Calculate the similarity score
for item in left_list:
    final_sum += (right_list[item] * item)

# Print the result
print(f'The similarity score is: {final_sum}')
