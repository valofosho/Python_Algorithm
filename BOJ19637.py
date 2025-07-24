import sys
input = sys.stdin.readline

# N, M -> 10**5 (100000)
namelist = []
lnlist = []
N, M = map(int, input().split())
for i in range(N):
    name, ln = map(str, input().split())
    ln = int(ln)
    namelist.append(name)
    lnlist.append(ln)

for _ in range(M):
    num = int(input())

    left, right = 0, len(lnlist) - 1
    while left <= right:
        mid = (left + right) // 2
        if lnlist[mid] < num:
            left = mid +1
        else:
            right = mid - 1
    print(namelist[right+1])