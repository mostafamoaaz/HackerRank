#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#
def max_pos_moves(n,r_q,c_q):
    # calculating up, down, left and right moves
    side_moves      = (n-1) * 2
    # calculating diagonal moves
    x,y             = min( abs(r_q - (n-1)), r_q),min( abs(c_q - (n-1)), c_q) #x,y are positions from boarders
    boarder_dist    = min(x,y)
    diagonal_moves  = (n-1) + 2*boarder_dist
    n_moves = side_moves + diagonal_moves
    # print(n_moves)
    return n_moves





def queensAttack(n, k, r_q, c_q, obstacles):
    # -1 to every coordinate because the input is one-indexed while the algorithm is zero-indexed 
    r_q -= 1
    c_q -= 1
    obstacles = set((x-1,y-1) for x,y in obstacles)
    #prepare the number of possible moves for Queen and return the number if no obstacles in the board
    n_moves = max_pos_moves(n,r_q,c_q)
    if not k:
        return n_moves
    #prepare number of moves with respect to the direction 
    directions ={
        'up': n - 1 - r_q,
        'down': r_q,
        'left': c_q,
        'right': n - 1 - c_q,
        'up_left': min(n - 1 - r_q, c_q),
        'up_right': min(n - 1 - r_q, n - 1 - c_q),
        'down_left': min(r_q, c_q),
        'down_right': min(r_q, n - 1 - c_q)
    }
    for obst in obstacles:
        x, y = obst
        if x == r_q:
            if y < c_q:
                directions['left'] = min(directions['left'], c_q - 1 - y)
            else:
                directions['right'] = min(directions['right'], y - 1 - c_q)
        elif y == c_q:
            if x < r_q:
                directions['down'] = min(directions['down'], r_q - 1 - x)
            else:
                directions['up'] = min(directions['up'], x - 1 - r_q)
        elif abs(x - r_q) == abs(y - c_q):
            if x < r_q and y < c_q:
                directions['down_left'] = min(directions['down_left'], min(r_q - 1 - x, c_q - 1 - y))
            elif x < r_q and y > c_q:
                directions['down_right'] = min(directions['down_right'], min(r_q - 1 - x, y - 1 - c_q))
            elif x > r_q and y < c_q:
                directions['up_left'] = min(directions['up_left'], min(x - 1 - r_q, c_q - 1 - y))
            else:
                directions['up_right'] = min(directions['up_right'], min(x - 1 - r_q, y - 1 - c_q))
    total_moves = sum(directions.values())
    return total_moves


n, r_q, c_q, k, obstacles = 4,4,4,0,[]
# max_pos_moves(n,r_q,c_q)
# moves_post(n,r_q,c_q)
print(queensAttack(n, k, r_q, c_q, obstacles))


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     k = int(first_multiple_input[1])

#     second_multiple_input = input().rstrip().split()

#     r_q = int(second_multiple_input[0])

#     c_q = int(second_multiple_input[1])

#     obstacles = []

#     for _ in range(k):
#         obstacles.append(list(map(int, input().rstrip().split())))

#     result = queensAttack(n, k, r_q, c_q, obstacles)

#     fptr.write(str(result) + '\n')

#     fptr.close()