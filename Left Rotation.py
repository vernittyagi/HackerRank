#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
#1 2 3 4 5
def rotLeft(a, d):
    i=0
    rotated = []
    while(i<d):
        rotated.append(a[i])
        i+=1
    a = a[d:] + rotated[:len(rotated)]
    return a
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
