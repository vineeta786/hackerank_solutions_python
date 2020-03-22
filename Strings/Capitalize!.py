

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    l = s.split(" ")
    width = len(l)
    for i in range(width):
        if(l[i].isalpha()):
            cap = list(l[i])
            cap[0] = cap[0].upper()
            l[i] = "".join(cap)
            cap.clear()
    res = " ".join(l)    
    return res

if __name__ == '__main__':