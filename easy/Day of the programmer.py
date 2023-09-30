#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#
#solution isnot correct.. had help from chatgpt
def dayOfProgrammer(year):
    
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0   :
        d = 12
    else :
        d = 13

    return str(d)+".09."+str(year)


print(dayOfProgrammer(1800))
print(dayOfProgrammer(2100))
print(dayOfProgrammer(1920))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     year = int(input().strip())

#     result = dayOfProgrammer(year)

#     fptr.write(result + '\n')

#     fptr.close()
