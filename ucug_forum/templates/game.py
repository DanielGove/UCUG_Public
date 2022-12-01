#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'gameWinner' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING colors as parameter.
#

def gameWinner(colors):
    # Brute force approach;
    # On Wendy's turn remove a W from the first string of 3 or more Ws
    # On Bob's turn remove a B from the first string of 3 or more Bs.
    
    # Player turn = Wendy if True else Bob
    remove_w = 0
    remove_b = 0
    consec_w = 0
    consec_b = 0
    for color in colors:
        if color == 'w':
            consec_w += 1
            if consec_b >= 3:
                remove_b += consec_b-2
            consec_b = 0
        else:
            consec_b += 1
            if consec_w >= 3:
                remove_w += consec_w-2
            consec_w = 0
    if consec_w >= 3:
        remove_w += consec_w - 2
    if consec_b >= 3:
        remove_b += consec_b - 2
    
    if remove_w == 0:
        return 'bob'

    if remove_w > remove_b-1:
        return 'wendy'
    else:
        return 'bob'
    
if __name__ == '__main__':
    assert(gameWinner("")) == 'bob'
    assert(gameWinner("w")) == 'bob'
    assert(gameWinner("ww")) == 'bob'
    assert(gameWinner("www")) == 'wendy'
    assert(gameWinner("bbb")) == 'bob'