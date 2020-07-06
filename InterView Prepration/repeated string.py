#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    lens = len(s)
    totalStringRep = n//lens
    extraChar = n%lens

    occ_A = s.count('a')*totalStringRep
    s = s[0:extraChar]
    #print(s)
    occ_A = occ_A + s.count('a')

    return occ_A

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
