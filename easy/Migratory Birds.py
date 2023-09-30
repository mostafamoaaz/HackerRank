#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    types =[0]*5
    for i in arr:
        types[i-1] += 1
    mostfreq = 0 
    print(types)
    for i in range(len(types)-1,-1,-1):
        print(mostfreq)
        if types[i] >= mostfreq:
            mostfreq = types[i]
            mostfreq_id = i+1
    return mostfreq_id
    
arr = [1,1,2,2,4,3,5,5]
print(migratoryBirds(arr))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr_count = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     result = migratoryBirds(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()
 