import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    N=int(input())
    Arr=[]
    count=1
    for i in range(N):
        a, b= map(int,input().split())
        Arr.append([a,b])
    Arr.sort()
    max=Arr[0][1]
    for j in range(1,N):
        if Arr[j][1]<max:
            count+=1
            max=Arr[j][1]
    print(count)