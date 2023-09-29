#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    maxval = min(b)
    minval= max(a)
    fac = []

    for i in range(minval,maxval+1):
        pot_fac = [i for x in a if i % x == 0]
        if len(pot_fac) == len(a):
            fac.append(pot_fac[0])
    result = 0
    for i in fac:
        pot_fac = [i for x in b if x % i == 0]
        if len(pot_fac) == len(b):
            result+=1
    return result

a = [2,4]
b = [16,32,96]
getTotalX(a,b)
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     m = int(first_multiple_input[1])

#     arr = list(map(int, input().rstrip().split()))

#     brr = list(map(int, input().rstrip().split()))

#     total = getTotalX(arr, brr)

#     fptr.write(str(total) + '\n')

#     fptr.close()
