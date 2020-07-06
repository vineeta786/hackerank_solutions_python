#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    seaLevel = 0
    valley = 0
    for level in s:
        if level == "D":
            seaLevel-=1
           
        elif level == "U": 
            seaLevel+=1
        
        if seaLevel == 0 and level =="U":
            valley+=1
    return valley
           


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
