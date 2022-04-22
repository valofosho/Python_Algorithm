def sol(arr, start, end, target, say):
    if start > end:
        say.append(0)
        return
    mid = (start + end) // 2
    if arr[mid][0] > target:
        return sol(arr, start, mid-1, target, say)
    elif arr[mid][0] < target:
        return sol(arr, mid+1, end, target, say)
    elif arr[mid][0] == target:
        say.append(arr[mid][1])
        return

import sys
from collections import Counter
input = sys.stdin.readline
N = int(input().rstrip())
ls = sorted(Counter(list(map(int,input().split()))).items(), key = lambda x : x[0])
M = int(input().rstrip())
lss = list(map(int,input().split()))
says=[]
lenN=len(ls)
for i in range(M):
    sol(ls, 0, lenN-1,lss[i],says)
print(" ".join(map(str,says)))
