def sorting(arr):
    for i in arr:
        if i < 0:
            m.append(i)
        elif i >= 0:
            p.append(i)
    m.sort()
    p.sort()
    sorted_arr = m + p
    return sorted_arr
import sys
input = sys.stdin.readline
N=int(input())
ls, m, p = [], [], []
for i in range(N):
    ls.append(int(input()))
sorted = sorting(ls)
print(*sorted, sep = '\n')