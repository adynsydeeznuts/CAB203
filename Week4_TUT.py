import math

S1 = { x for x in range(1, 13) if 12 % x == 0}
S2 = { x for x in range(1, 73) if 72 % x == 0 and math.sqrt(x) % 1 != 0}
S3 = { x for x in range(1, 65) if x % 5 == 0}

S = {1, 2, 3, 5, 6, 8}
T = {2, 3, 5, 10, 15, 22}
U = {1, 3, 4, 6, 22, 8}

S4 = { x for x in S & T and S - U}

def S5(x):
    return { y for y in range (0, 100) if y % x == 0}

def S6(S, U):
    if(S <= U):
        return U - S
    else:
        return "S is not a subset of U"

S = {1, 2, 3, 4}
U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(S6(S, U))