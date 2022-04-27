

from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
for i in range(N):
    numP, place = map(int,input().split())
    imp = deque(list(map(int,input().split())))
    maximum = max(imp)
    cnt = 1
    while imp[0] != max(imp):
        imp.rotate(-1)
        cnt += 1
        if imp[place]
