import sys
input = sys.stdin.readline
N = int(input())
ls = []
for i in range(N):
    a = list(map(int,input().split()))
    ls.append(a)
ls.sort(key=lambda x:(x[1], x[0]))
for j in range(len(ls)):
    print(" ".join(map(str, ls[j])))