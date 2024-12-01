#!/usr/bin/env python3

# Define lists for use.
left_list = []
right_list = []

# Open file and put data into lists
with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split('  ')
        line[1] = line[1].strip()
        left_list.append(int(line[0]))
        right_list.append(int(line[1]))

# Sort data
left_list.sort()
right_list.sort()

# Find the deltas between the left and right lists
final_list = [i for i in zip(left_list, right_list)]
final_list = [abs(i[0] - i[1]) for i in final_list]

# Find the sum
print(f'The sum of the differences is: {sum(final_list)}')
