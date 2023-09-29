#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    result = 0
    # if len(s) == 1 and m == 1 and d == s[0]:
    #     return 1

    for i in range(len(s[:-m])+1):
        print(s[i])
        day = 0
        month = 0
        while month != m:
            day += s[i+month]
            month += 1
        if day == d:
            result +=1
    return result

# s = [1,2,1,3,2]
# d = 3
# m = 2

# s = [1,1,1,1,1,1]
# d = 3
# m = 2

# s = [4]
# d = 4
# m = 1

# r = birthday(s, d, m)
# print(r)
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     s = list(map(int, input().rstrip().split()))

#     first_multiple_input = input().rstrip().split()

#     d = int(first_multiple_input[0])

#     m = int(first_multiple_input[1])

#     result = birthday(s, d, m)

#     fptr.write(str(result) + '\n')

#     fptr.close()
