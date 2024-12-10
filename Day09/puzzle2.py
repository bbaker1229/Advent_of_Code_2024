#!/usr/bin/env python3

disk_dict = {}

# Read file
with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = list(line.strip())
line = [int(i) for i in line]

# find files
file_id = 0
for file_ind in range(0, len(line), 2):
    file_size = line[file_ind]
    if file_ind == (len(line) - 1):
        space_size = 0
    else:
        space_size = line[file_ind+1]
    disk_dict[file_id] = [str(file_id)]*file_size + ['.']*space_size
    file_id += 1

# Move files
for end_file_id in range(len(disk_dict)-1, -1, -1):
    for front_file_id in range(end_file_id):
        end_file = disk_dict[end_file_id]
        front_file = disk_dict[front_file_id]
        end_file_section = [i for i in end_file if i == str(end_file_id)]
        if len(end_file_section) == 0:
            continue
        end_file_ending = end_file[len(end_file_section):]
        front_file_section = [i for i in front_file if i != '.']
        front_file_space = front_file[len(front_file_section):]
        if len(end_file_section) <= len(front_file_space):
            new_front_space = len(front_file_space) - len(end_file_section)
            new_front_file = front_file_section + end_file_section + ['.']*new_front_space
            new_end_space = ['.']*len(end_file_section) + end_file_ending
            disk_dict[front_file_id] = new_front_file
            disk_dict[end_file_id] = new_end_space

# Calculate the checksum
cnt = 0
checksum = 0
for file_id in disk_dict.keys():
    file_info = disk_dict[file_id]
    for item in file_info:
        if item != '.':
            value = int(item) * cnt
            checksum += value
        cnt += 1

print(f"The checksum is: {checksum}")
