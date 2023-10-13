#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
def ranking(ranked):
    # constructing the leaderboard ranking R:
    R = [0] * len(ranked)
    for i in range(len(ranked)):
        if not i :
            R[i] = 1
        if ranked[i] == ranked[i-1]:
            R[i] = R[i-1]
        else:
            R[i] = R[i-1] + 1
    return R


def climbingLeaderboard(ranked, player):
    ranked.append(0)
    R = ranking(ranked)

    R.reverse()
    ranked.reverse()
    result = []
    r=0
    for p in player:
        for i in range(r,len(ranked)):
            if ranked[i] == p:
                result.append(R[i])
                r = i
                break
            elif ranked[i] > p:
                result.append(R[i]+1)
                r = i
                break
    while len(player) != len(result):
        result.append(1)


    return result


ranked = [1]
player = [1,1]
r = climbingLeaderboard(ranked, player)
print(r)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     ranked_count = int(input().strip())

#     ranked = list(map(int, input().rstrip().split()))

#     player_count = int(input().strip())

#     player = list(map(int, input().rstrip().split()))

#     result = climbingLeaderboard(ranked, player)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
