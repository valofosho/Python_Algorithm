def q_push(q, x):
    q.append(x)
    return q
def q_pop(q):
    if q:
        print(q[0])
        q.remove(q[0])
        return q
    else:
        print(-1)
        return q
def q_size(q):
    q_len=len(q)
    print(q_len)
    return q

def q_empty(q):
    if not q:
        print(1)
        return q
    if q:
        print(0)
        return q
def q_front(q):
    if not q:
        print(-1)
        return q
    else:
        print(q[0])
        return q

def q_back(q):
    if not q:
        print(-1)
        return q
    else:
        print(q[-1])
        return q

import sys
input=sys.stdin.readline
N=int(input())
q=[]
for i in range(N):
    op=input().split()
    if "push" in op:
        x=op[1]
        q=q_push(q,x)
    elif "pop" in op:
        q=q_pop(q)
    elif "size" in op:
        q=q_size(q)
    elif "empty" in op:
        q=q_empty(q)
    elif "front" in op:
        q = q_front(q)
    elif "back" in op:
        q=q_back(q)