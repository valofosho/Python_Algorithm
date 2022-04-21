import sys
input = sys.stdin.readline
N = int(input())
line = list(map(int,input().split()))
ls = []
for i in line:
    if i in ls:
        pass
    else:
        ls.append(i)
ls.sort(key = lambda x: x)
print(" ".join(map(str,ls)))