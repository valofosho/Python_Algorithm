import sys
input=sys.stdin.readline
N=int(input())
cnt=[0 for i in range(10001)]
ls=[]
for i in range(N):
    temp=int(input())
    cnt[temp]+=1
for i in range(10001):
    if cnt[i]>0:
        for j in range(cnt[i]):
            print(i)
