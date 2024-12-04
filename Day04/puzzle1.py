#!/usr/bin/env python3

grid_map = []

# Open file process data
with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = list(line.strip())
        grid_map.append(line)

print(f"Number of rows: {len(grid_map)}")
print(f"Number of cols: {len(grid_map[0])}")

# search hortz left to right
horz_left_cnt = 0
for line in grid_map:
    for ind in range(0,len(line)-3):
        if (line[ind] == 'X') and (line[ind+1] == 'M') and (line[ind+2] == 'A') and (line[ind+3] == 'S'):
            horz_left_cnt += 1
# print(horz_left_cnt)

# search hortz right to left
horz_right_cnt = 0
for line in grid_map:
    for ind in range(len(line)-1, -1+3, -1):
        if (line[ind] == 'X') and (line[ind-1] == 'M') and (line[ind-2] == 'A') and (line[ind-3] == 'S'):
            horz_right_cnt += 1
# print(horz_right_cnt)

# search vert down
vert_down_cnt = 0
for row in range(len(grid_map)-3):
    line = grid_map[row]
    for col in range(0,len(line)):
        if (grid_map[row][col] == 'X') and (grid_map[row+1][col] == 'M') and (grid_map[row+2][col] == 'A') and (grid_map[row+3][col] == 'S'):
            vert_down_cnt += 1
# print(vert_down_cnt)

# search vert up
vert_up_cnt = 0
for row in range(len(grid_map)-1, -1+3, -1):
    line = grid_map[row]
    for col in range(0,len(line)):
        if (grid_map[row][col] == 'X') and (grid_map[row-1][col] == 'M') and (grid_map[row-2][col] == 'A') and (grid_map[row-3][col] == 'S'):
            vert_up_cnt += 1
# print(vert_up_cnt)

# search down and right
down_right_cnt = 0
for row in range(len(grid_map)-3):
    line = grid_map[row]
    for col in range(0,len(line)-3):
        if (grid_map[row][col] == 'X') and (grid_map[row+1][col+1] == 'M') and (grid_map[row+2][col+2] == 'A') and (grid_map[row+3][col+3] == 'S'):
            down_right_cnt += 1
# print(down_right_cnt)

# search down and left
down_left_cnt = 0
for row in range(len(grid_map)-3):
    line = grid_map[row]
    for col in range(len(line)-1, -1+3, -1):
        if (grid_map[row][col] == 'X') and (grid_map[row+1][col-1] == 'M') and (grid_map[row+2][col-2] == 'A') and (grid_map[row+3][col-3] == 'S'):
            down_left_cnt += 1
# print(down_left_cnt)

# search up and right
up_right_cnt = 0
for row in range(len(grid_map)-1, -1+3, -1):
    line = grid_map[row]
    for col in range(0,len(line)-3):
        if (grid_map[row][col] == 'X') and (grid_map[row-1][col+1] == 'M') and (grid_map[row-2][col+2] == 'A') and (grid_map[row-3][col+3] == 'S'):
            up_right_cnt += 1
# print(up_right_cnt)

# search up and left
up_left_cnt = 0
for row in range(len(grid_map)-1, -1+3, -1):
    line = grid_map[row]
    for col in range(len(line)-1, -1+3, -1):
        if (grid_map[row][col] == 'X') and (grid_map[row-1][col-1] == 'M') and (grid_map[row-2][col-2] == 'A') and (grid_map[row-3][col-3] == 'S'):
            up_left_cnt += 1
# print(up_left_cnt)

# Find the total count
total_cnt = horz_left_cnt + horz_right_cnt + vert_down_cnt + vert_up_cnt + down_right_cnt + down_left_cnt + up_right_cnt + up_left_cnt
print(f"The total count is: {total_cnt}")