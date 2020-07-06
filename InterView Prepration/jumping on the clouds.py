#!/bin/python3

import math
import os
import random
import re
import sys
# 0 0 0 0 1 0
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = -1
    n = len(c)
    i=0
    while i<n:
        if i<n-2 and c[i+2]==0:
            i+=1
        jumps+=1
        i+=1
    # i = 0
    # while i<=n-2 :
    #     if c[i]==0 and c[i+2]==0 and n-i>1:
    #         jumps+=1
    #         i+=2
    #         print("2 step jump curr position: "+str(i)+" "+str(c[i]))
    #     elif c[i]==0 and c[i+1] == 0:
    #         jumps+=1
    #         i+=1    
    #         print("1 step jump curr position :"+str(i)+" "+str(c[i]))
        
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
