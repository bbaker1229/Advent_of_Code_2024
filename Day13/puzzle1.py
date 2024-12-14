#!/usr/bin/env python3

# Create the required functions
def find_best(AX, AY, PX, BX, BY, PY):
    best_sum = 201
    best = [-1, -1]
    for X in range(101):
        for Y in range(101):
            if (PX == (AX*X+BX*Y)) and (PY == (AY*X+BY*Y)):
                if (best_sum > (X+Y)):
                    best_sum = (X+Y)
                    best = [X, Y]
    return best

# Create the required variables
total = 0
cnt = 1

with open("input.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if "Button A" in line:
            line = line.split(':')
            line = line[1].strip()
            line = line.split(',')
            line = [item.strip() for item in line]
            AX = int(line[0][1:])
            AY = int(line[1][1:])
        elif "Button B" in line:
            line = line.split(':')
            line = line[1].strip()
            line = line.split(',')
            line = [item.strip() for item in line]
            BX = int(line[0][1:])
            BY = int(line[1][1:])
        elif "Prize" in line:
            line = line.split(':')
            line = line[1].strip()
            line = line.split(',')
            line = [item.strip() for item in line]
            PX = int(line[0][2:])
            PY = int(line[1][2:])
            print(f"Equation1 is: {AX}x + {BX}y = {PX}")
            print(f"Equation2 is: {AY}x + {BY}y = {PY}")
            print(f"The full equation is: {AX+AY}x + {BX+BY}y = {PX+PY}")
            result = find_best(AX, AY, PX, BX, BY, PY)
            if (result[0] != -1) and (result[1] != -1):
                total += (3 * result[0] + result[1])
                print(f"Game {cnt} is possible with: {result}.  Cost for this game: {3 * result[0] + result[1]}.  Running total is: {total}")
            else:
                print(f"Game {cnt} is not possible.")
        else:
            cnt += 1

# Print the result
print(f"The total number of tokens needed is: {total}")
