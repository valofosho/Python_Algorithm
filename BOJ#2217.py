N=int(input())
ans=[]
ls=[]
for i in range(N):
    ls.append(int(input()))
ls.sort(reverse=True)
for i in range(N):
    ans.append(ls[i]*(i+1))
print(max(ans))
