# deque 이용하지 않고 쓸까나
def push_front(D,x):
    D.appendleft(x)
    return D
def push_back(D,x):
    D.append(x)
    return D
def pop_front(D):
    if not D:
        print(-1)
        return D
    else:
        D.popleft()
        return D
def pop_back(D):
    if not D:
        print(-1)
        return D
    else:
        D.pop()
        return D
def d_size(D):
    print(len(D))
    return D
def d_empty(D):
    if not D:
        print(1)
        return D
    else:
        print(0)
        return D
def front(D):
    if not D:
        print(-1)
        return D
    else:
        print(D[0])
        return D
def back(D):
    if not D:
        print(-1)
        return D
    else:
        print(D[-1])
        return D




import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
deq=deque()
for i in range(N):
    op=input().split()
    if "push_front" in op:
        x=op[1]
        deq=push_front(deq,x)
    elif "push_back" in op:
        x=op[1]
        deq=push_back(deq,x)
    elif "pop_front" in op:
        deq=pop_front(deq,x)


        op = input().split()
        if "push" in op:
            x = op[1]
            q = q_push(q, x)
        elif "pop" in op:
            q = q_pop(q)
        elif "size" in op:
            q = q_size(q)
        elif "empty" in op:
            q = q_empty(q)
        elif "front" in op:
            q = q_front(q)
        elif "back" in op:
            q = q_back(q)