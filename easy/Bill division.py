#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    b_actual = 0
    for i in range(len(bill)) :
        if i != k:
            b_actual += bill[i]

    b_actual = b_actual/2
    if b == b_actual :
        print("Bon Appetit")
    else:
        print(str(int(b-b_actual))) 

bonAppetit([3,10,2,9], 1, 12)
# if __name__ == '__main__':
#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     k = int(first_multiple_input[1])

#     bill = list(map(int, input().rstrip().split()))

#     b = int(input().strip())

#     bonAppetit(bill, k, b)
