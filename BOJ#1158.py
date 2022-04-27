from collections import deque
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
deq = deque([ i+1 for i in range(N)])
ans = []
while len(deq)>0:
    deq.rotate(-(K-1))
    ans.append(deq[0])
    deq.popleft()
print('<'+', '.join(map(str,ans))+'>')