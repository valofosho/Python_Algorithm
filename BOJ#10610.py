N=list(map(str,input().split()))
ls=[]
for i in range(len(N[0])):
    ls.append(int(N[0][i]))
mul=0
ans=""
for i in ls:
    mul+=i
if mul%3!=0 or 0 not in ls:
    print(-1)
else:
    ls.sort(reverse=True)
    ans=''.join(map(str,ls))
    print(ans)
