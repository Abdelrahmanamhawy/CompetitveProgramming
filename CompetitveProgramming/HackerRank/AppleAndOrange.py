#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    appCount=0
    orCount=0
    for i in range (m):
        if(apples[i]+a>=s and apples[i]+a<=t):
         appCount+=1
    for i in range (n) :
        if(oranges[i]+b>=s and oranges[i]+b<=t):
          orCount+=1
    print(appCount)
    print(orCount)
    


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
