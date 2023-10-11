#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
def magicSquare(p):
    magic_constant = 15

    #checking each row itering through as patchs of 3 numbers
    for i in range(0,9,3):
        if sum(p[i:i+3]) != magic_constant:
            return False
    #checking each column itering through with jump step of 3
    for i in range(3):
        if sum(p[i::3]) != magic_constant:
            return False
    #checking diagonals:
    if sum(p[::3+1]) != magic_constant or sum(p[2:8:2]) != magic_constant:
        return False
    return True
def genMagicSquares():
    magic_squares = []
    n = 9
    permutations = itertools.permutations(range(1,n+1))
    c = 0
    for p in permutations:
        if magicSquare(p):
            magic_squares.append(list(p))
    return magic_squares
def formingMagicSquare(s):
    magics = genMagicSquares()
    flatten = [e for r in s for e in r]
    costs = []
    for magic in magics:
        cost = 0
        for j in range(9):
            cost += abs(flatten[j] - magic[j])
        costs.append(cost)
    return min(costs)



# magics = [[2, 7, 6, 9, 5, 1, 4, 3, 8], [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 3, 8, 9, 5, 1, 2, 7, 6], [4, 9, 2, 3, 5, 7, 8, 1, 6], [6, 1, 8, 7, 5, 3, 2, 9, 4], [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 1, 6, 3, 5, 7, 4, 9, 2], [8, 3, 4, 1, 5, 9, 6, 7, 2]]
s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
s = [[4, 9, 2],
[3, 5, 7],
[8, 1, 5]]
print(formingMagicSquare(s))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = []

#     for _ in range(3):
#         s.append(list(map(int, input().rstrip().split())))

#     result = formingMagicSquare(s)

#     fptr.write(str(result) + '\n')

#     fptr.close()
