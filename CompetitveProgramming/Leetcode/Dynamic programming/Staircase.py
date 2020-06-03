rows=int(input())
i=rows-1
shebak="#"
while(i>=0):
    
    for j in range(rows):
        if(j>=i):
         print(shebak,end="")
        else:
         print(" ",end="")

    print(" ")
    i-=1
