def check(arr, target, start, end, cnt):
    if start > end:
        return 0
    mid = (start + end) // 2
    if arr[mid] == target:
        cnt += 1



import sys
input = sys.stdin.readline
N = int(input().rstrip())
ls = list(map(int,input().split()))
ls.sort()
M = int(input().rstrip())
lss = list(map(int,input().split()))
num = []
cnt = 0
for i in range(M):
    cnt = ls.count(lss[i])
    num.append(cnt)
    cnt = 0
print(" ".join(map(str, num)))