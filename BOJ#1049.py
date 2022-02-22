#BOJ1049 (기타줄)
N,M=map(int, input().split())
A,B=[],[]
ans=0
for _ in range(M):
    a,b=(map(int, input().split()))
    A.append(a)
    B.append(b)

#min(A)=min(SET), min(B)=min(single)
min_s= min(min(A),min(B)*6)     #min(set)

while N:
    if N>6:
        ans+=min_s
        N-=6
    if N<=6:
        min_ss=min(min(A),min(B)*N)
        ans+=min_ss
        print(ans)
        break
