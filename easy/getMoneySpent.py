#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    
    keyboards_r = sorted(keyboards, reverse=True)
    drives_r = sorted(drives, reverse=True)
    pairs = [[x,y] for x in keyboards_r for y in drives_r]
    if keyboards_r[-1] >= b or drives_r[-1] >= b:
        return -1
    best_price = -1
    for i in pairs:
        price = i[0] + i[1]
        if price > b :
            pass
        elif price == b:
            return price
        elif price < b and price > best_price:
            best_price = price
    return best_price
            


#--------------------------------------------------------------------------
k = [50, 10]
d = [5, 2, 8]
b = 10
print(getMoneySpent(k,d,b))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     bnm = input().split()

#     b = int(bnm[0])

#     n = int(bnm[1])

#     m = int(bnm[2])

#     keyboards = list(map(int, input().rstrip().split()))

#     drives = list(map(int, input().rstrip().split()))

#     #
#     # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
#     #

#     moneySpent = getMoneySpent(keyboards, drives, b)

#     fptr.write(str(moneySpent) + '\n')

#     fptr.close()
