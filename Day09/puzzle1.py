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

# Move blocks
for end_file_id in range(len(disk_dict)-1, -1, -1):
    for front_file_id in range(len(disk_dict)):
        end_file = disk_dict[end_file_id]
        if set(end_file) == {'.'}:
            break
        front_file = disk_dict[front_file_id]
        if '.' not in front_file:
            continue
        while (set(end_file) != {'.'}) and ('.' in front_file) and (front_file_id < end_file_id):
            for end_space_ind in range(len(end_file)-1, -1, -1):
                if end_file[end_space_ind] != '.':
                    value = end_file[end_space_ind]
                    end_file[end_space_ind] = '.'
                    break
            for front_space_ind in range(len(front_file)):
                if front_file[front_space_ind] == '.':
                    front_file[front_space_ind] = value
                    break

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
