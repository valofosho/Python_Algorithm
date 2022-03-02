N=int(input())
ls=list(map(int,input().split()))
ls.sort()
a=ls[0]
j=[a]
for i in range(1,N):
    j.append(j[i-1]+ls[i])
ans=0
for i in j:
    ans+=i
print(ans)