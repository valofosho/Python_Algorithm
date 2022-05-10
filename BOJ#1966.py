from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
for i in range(N):
    numP, place = map(int,input().split())
    imp = deque(list(map(int,input().split())))
    order = deque([])
    for j in range(numP):
        while j != place:
            order.append(0)
        order.append('a')
    maximum = max(imp)
    cnt = 0
    stop = 0
    while stop != 1 :
        if imp[0] == maximum:
            if order[0] != 'a':
                imp.popleft()
                maximum = max(imp)
                cnt += 1
            else:
                print(cnt)
                stop += 1
        else:
            imp.rotate(-1)
            order.rotate(-1)
            cnt += 1


"""
문제 예시 
3
1 0
5
4 2
1 2 3 4
6 0 
1 1 9 1 1 1

중요 포인트
! 중요도는 1이상 9이하 정수
! 중요도는 겹칠 수 있다.

해결방안
! 
"""