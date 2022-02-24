#BOJ2839 (설탕 배달)
N=int(input())
a, b = 3, 5
ans=[]
for i in range((N//a)+1):
    for j in range((N//b)+1):
        if (3*i)+(5*j)==N:
            ans.append(i+j)
if len(ans)==0:
    print(-1)
else:
    print(min(ans))