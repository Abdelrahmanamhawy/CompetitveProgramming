if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

m=max(arr)
flag=True
c=0
i=0
while(i<n):
    if(arr[i]==m):
        del arr[i]
        i=0
        n-=1
    else:
        i+=1
print(max(arr))
