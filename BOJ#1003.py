"""
def fibonacci(N):
    m=list()
    if N==0:
        m.append(0)
        return m
    elif N==1:
        m.append(1)
        return m
    else:
        return fibonacci(N-1) + fibonacci(N-2)
def fo(m):
    a=[m.count(0), m.count(1)]
    a=str(a)[1:-1]
    return a
T=int(input())
for _ in range(T):
    N=int(input())
    print(fo(fibonacci(N)))
"""
"""

def fibo(N):
    if N==0:
        print("0")
        return 0
    elif N==1:
        print("1")
        return 1
    else:
        return fibo(N-1) + fibo(N-2)

print(fibo(5))
"""


T=int(input())
zero=[1,0]
one=[0,1]
def fibo(n):
    if len(zero) <=n:
        for i in range(len(zero),n+1):
            zero.append(one[i-1])
            one.append(one[i-2]+one[i-1])
        print(zero[i],one[i])
    else:
        print(zero[n],one[n])
for i in range(T):
    n=int(input())
    fibo(n)
