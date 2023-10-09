#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    flag = [1] * n
    pair = 0
    for i in range(n):
        if flag[i] :
            for j in range(i+1,n):
                print (i,j)
                if ar[i] == ar[j] and flag[j]:
                    pair += 1
                    flag[i],flag[j] = 0 ,0
                    print(flag)
                    break

    print(pair)


    
sockMerchant(6 ,[1,2,1,2,1,2])
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     ar = list(map(int, input().rstrip().split()))

#     result = sockMerchant(n, ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()
