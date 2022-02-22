#BOJ1541 (잃어버린 괄호)
N=input().split('-')
ans=[]
for i in N:
    count=0
    num=i.split('+')
    for j in num:
        count+=int(j)
    ans.append(count)
answer=ans[0]
for i in range(1,len(ans)):
    answer-=ans[i]
print(answer)
