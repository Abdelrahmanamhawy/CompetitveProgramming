#!/bin/python3

import math
import random

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    
    print(len(arr))
    while(len(arr)>1):
        shortest=min(arr)
        for i in range(len(arr)):
            arr[i]-=shortest
        arr=[i for i in arr if i!=0]
        if(len(arr)!=0):
           print(len(arr))

n = int(input())

arr = list(map(int, input().rstrip().split()))

result = cutTheSticks(arr)
