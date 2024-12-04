#!/usr/bin/env python3

grid_map = []

# Open file process data
with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = list(line.strip())
        grid_map.append(line)

print(f"Number of rows: {len(grid_map)}")
print(f"Number of cols: {len(grid_map[0])}")

# search down and up
down_up_cnt = 0
for row in range(1, len(grid_map)-1):
    line = grid_map[row]
    for col in range(1,len(line)-1):
        if (grid_map[row][col] == 'A') and (grid_map[row-1][col-1] == 'M') and (grid_map[row+1][col+1] == 'S') and (grid_map[row+1][col-1] == 'M') and (grid_map[row-1][col+1] == 'S'):
            down_up_cnt += 1
# print(down_up_cnt)

# search down and down
down_down_cnt = 0
for row in range(1, len(grid_map)-1):
    line = grid_map[row]
    for col in range(1,len(line)-1):
        if (grid_map[row][col] == 'A') and (grid_map[row-1][col-1] == 'M') and (grid_map[row+1][col+1] == 'S') and (grid_map[row-1][col+1] == 'M') and (grid_map[row+1][col-1] == 'S'):
            down_down_cnt += 1
# print(down_down_cnt)

# search up and up
up_up_cnt = 0
for row in range(1, len(grid_map)-1):
    line = grid_map[row]
    for col in range(1,len(line)-1):
        if (grid_map[row][col] == 'A') and (grid_map[row-1][col-1] == 'S') and (grid_map[row+1][col+1] == 'M') and (grid_map[row+1][col-1] == 'M') and (grid_map[row-1][col+1] == 'S'):
            up_up_cnt += 1
# print(up_up_cnt)

# search up and down
up_down_cnt = 0
for row in range(1, len(grid_map)-1):
    line = grid_map[row]
    for col in range(1,len(line)-1):
        if (grid_map[row][col] == 'A') and (grid_map[row-1][col-1] == 'S') and (grid_map[row+1][col+1] == 'M') and (grid_map[row-1][col+1] == 'M') and (grid_map[row+1][col-1] == 'S'):
            up_down_cnt += 1
# print(up_down_cnt)

total_cnt = down_up_cnt + down_down_cnt + up_down_cnt + up_up_cnt
print(f"The total count is: {total_cnt}")
