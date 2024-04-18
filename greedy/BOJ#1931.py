N=int(input())
ls=[]
ans=[]
for i in range(N):
    ls.append(list(map(int,input().split())))
ls.sort(key=lambda x: (x[1],x[0]))
Ft, count=0 ,0
for start, end in ls:
    if start>=Ft:
        count+=1
        Ft=end
print(count)