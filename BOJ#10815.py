
def check(arr, target, start, end):
    if start > end :
        return 0
    mid = (start + end) // 2
    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return check(arr, target, start, mid - 1)
    elif arr[mid] < target:
        return check(arr, target, mid + 1, end)

import sys
input=sys.stdin.readline
N=int(input())
arr=list(map(int,input().split()))
M=int(input())
comp=list(map(int,input().split()))
arr.sort()
ans=[]
for i in range(M):
    ans.append(check(arr,comp[i],0,N-1))
print(*ans,sep=' ')