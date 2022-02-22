#BOJ11047 (동전)
N,K=map(int,input().split())
wons=[]
for i in range(N):
    wons.append(int(input()))

count=0
for _ in reversed(wons):
    if K == 0 :
        break
    count += K//_
    K %= _
print(count)
