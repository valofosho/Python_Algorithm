#BOJ1026 (보물)
N= int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
ans=0
for _ in range(len(A)):
    ans+=A[_]*max(B)
    B.remove(max(B))
print(ans)