#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    minimum = scores[0]
    maximum = scores[0]
    min_count = 0
    max_count = 0

    for i in scores[1:] :
        if i > maximum:
            maximum = i
            max_count +=1
        elif i < minimum:
            minimum = i
            min_count +=1
    
    return [max_count,min_count]
# scores = [10,11,5,10,5,11,55,4,56,2] 
# x = breakingRecords(scores)
# print(x)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
