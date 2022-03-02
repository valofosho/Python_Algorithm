N=int(input())
a, b, c,= 300, 60, 10
A, B, C = 0, 0, 0
if N%10!=0:
    print(-1)
else:
    A=N//a
    N=N%a
    B=N//b
    N=N%b
    C=N//c
    N=N%c
    print(A,B,C)