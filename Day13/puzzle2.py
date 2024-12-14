#!/usr/bin/env python3

# Create the required functions
def computeGCD(x, y):
    while(y):
        x, y = y, x % y
    return abs(x)

def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y

def checker(AX, A, BX, B, PX):
    if (PX == (A*AX + B*BX)):
        return True
    return False

def solve_de(A, B, C):
    d = computeGCD(A, B)
    if (C % d == 0):
        d, xo, yo = gcdExtended(A, B)
        k = (0 - xo * C // d) * d // B
        result = [(xo * C//d, B//d), (yo * C//d, -A//d)]
        return result
    else:
        # print('No Solution')
        return [-1, -1]

# Create the required variables
total = 0
cnt = 1

# Read input file
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
            PX = int(line[0][2:]) + 10000000000000
            PY = int(line[1][2:]) + 10000000000000
            # print(f"Equation1 is: {AX}x + {BX}y = {PX}")
            # print(f"Equation2 is: {AY}x + {BY}y = {PY}")
            # print(f"The full equation is: {AX+AY}x + {BX+BY}y = {PX+PY}")
            result1 = solve_de(AX, BX, PX)
            result2 = solve_de(AY, BY, PY)
            if (result1[0] != -1) and (result1[1] != -1) and (result2[0] != -1) and (result2[1] != -1):
                k2 = (result1[1][1]*result1[0][0] - result1[0][1]*result1[1][0]-result1[1][1]*result2[0][0]+result1[0][1]*result2[1][0]) // (result2[0][1]*result1[1][1] - result1[0][1]*result2[1][1])
                result = [result2[0][0]+result2[0][1]*k2, result2[1][0] + result2[1][1]*k2]
                if (checker(AX, result[0], BX, result[1], PX)) and (checker(AY, result[0], BY, result[1], PY)):
                    total += (3 * result[0] + result[1])
                    # print(f"Game {cnt} is possible with: {result}.  Cost for this game: {3 * result[0] + result[1]}.  Running total is: {total}")
            else:
                # print(f"Game {cnt} is not possible.")
                pass
        else:
            cnt += 1

# Print the result
print(f"The total number of tokens needed is: {total}")
