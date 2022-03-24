def sorting(arr):
    for i in range(len(arr)):
        if arr[i] >= 0:
            p.append(arr[i])
        else:
            m.append(arr[i])
    m.sort()
    p.sort()
    ans=m+p
    return ans

import sys
input=sys.stdin.readline
N=int(input())
ls, m, p=[], [], []

for i in range(N):
    ls.append(int(input()))
answer=sorting(ls)
print(*answer, sep='\n')