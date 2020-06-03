#!/bin/python3

import os
import sys
import math
   
def pageCount(n,p):
    front=1
    back=n
    minx=(p-front)/2
    miny=(back-p)/2
     #Same page
    if(p==back or p==front):
        return 0
    #First page after first or page before last ===1
    if((p-front<=1) or ((back-p<=1) and back%2==0)):
        return 1
    #Same page : 5&4
    if(back-p<=1 and back%2==1 ):
     return 0
   

    #Else,Find the differences between them and divide by two to get how many 2 pages are there betweeen them
    return math.floor(min(p/2,n/2-p/2))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
