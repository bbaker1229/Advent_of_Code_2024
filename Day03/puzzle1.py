#!/usr/bin/env python3
import re

# Create variables to use
pattern = r'mul\([0-9]{,3},[0-9]{,3}\)'
group_pattern = r'mul\(([0-9]{,3}),([0-9]{,3})\)'
total = 0

# Open file and put data into lists
with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        locations = [(m.span()) for m in re.finditer(pattern, line)]
        for item in locations:
            temp = line[item[0]:item[1]]
            match = re.search(group_pattern, temp)
            total += (int(match.group(1)) * int(match.group(2)))

# Print the total result of the multiplications
print(f"The total is: {total}")
