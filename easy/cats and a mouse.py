#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    zx = abs(x-z)
    zy = abs(y-z)
    if zx == zy:
        return "Mouse C"
    elif zx < zy:
        return "Cat A"
    elif zx > zy:
        return "Cat B"
    
print(catAndMouse(0,10,5))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input())

#     for q_itr in range(q):
#         xyz = input().split()

#         x = int(xyz[0])

#         y = int(xyz[1])

#         z = int(xyz[2])

#         result = catAndMouse(x, y, z)

#         fptr.write(result + '\n')

#     fptr.close()
