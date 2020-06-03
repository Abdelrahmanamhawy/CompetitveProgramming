#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
   Right=0
   Left=0
   tmp=n-1
   for i in range(n*n):
      for j in range(n):
        if(i==j):
         Left+=arr[i][j]
        if(j==tmp):
         Right+=arr[i][j]
      tmp-=1 

   return(abs(Left-Right))
     
  


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
