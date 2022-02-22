#no.11047 (동전)
"""
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
"""

#1026 (보물)
"""
N= int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
ans=0
for _ in range(len(A)):
    ans+=A[_]*max(B)
    B.remove(max(B))
print(ans)
"""

#5585(거스름돈)
"""
N=int(input())
A=[500,100,50,10,5,1]
mon=1000-N
counter=0
for _ in range(len(A)):
    if N==0:
        break
    counter+=mon//A[_]
    mon=mon%A[_]
print(counter)
"""

#1439 (뒤집기)
"""
N=list(map(str,input()))
count=0
for _ in range(len(N)-1):
    if N[_]!=N[_+1]:
        count+=1
count=(count+1)//2
print(count)
"""

#1049 (기타줄)-복잡한 풀이 + 문제 잘못 이해한 ver
"""
N,M=map(int, input().split())
A=list()
counter=1001

for _ in range(M):
    A.append(list(map(int, input().split())))
if N%6==0: #N이 6의 배수인 경우
    for __ in range(M):
        if (A[__][0]>= A[__][1]*N)& (counter>= A[__][1]*N):
            counter=A[__][1]*N
        elif (A[__][0]<A[__][1]*N)& (counter>=A[__][0]):
            counter=A[__][0]
        else:
            counter=counter
    counter=counter*(N//6)
elif N%6 !=0 & N>6: #N이 6의 배수가 아니며 6보다 큰 경우
    Na=N-(N%6)
    Nb=N%6
    for __ in range(M):
        if (A[__][0] >= A[__][1] * Na) & (counter >= A[__][1] * Na):
            counter = A[__][1] * Na  # 단일이 세트보다 싼 경우
        elif (A[__][0] < A[__][1] * Na) & (counter >= A[__][0]):
            counter = A[__][0]  # 세트가 단일에 비해 싼 경우
        else:
            counter = counter
    for __ in range(M):
        if (A[__][0] >= A[__][1] * Nb) & (counter >= A[__][1] * Nb):
            counter += A[__][1] * Nb  # 단일이 세트보다 싼 경우
        elif (A[__][0] < A[__][1] * Nb) & (counter >= A[__][0]):
            counter += A[__][0]  # 세트가 단일에 비해 싼 경우
        else:
            counter = counter


elif N%6 !=0 & N<6: #N이 6의 배수가 아니며 6보다 작은 경우
    for __ in range(M):
        if (A[__][0]>= A[__][1]*N)& (counter>= A[__][1]*N):
            counter=A[__][1]*N #단일이 세트보다 싼 경우
        elif (A[__][0]<A[__][1]*N)& (counter>=A[__][0]):
            counter=A[__][0] #세트가 단일에 비해 싼 경우
        else:
            counter=counter



print(counter)
"""

#1049(기타줄)
"""
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
"""

#2864 5와 6의 차이
"""
N,M=map(str,input().split())
min=int(N.replace('6','5'))+int(M.replace('6','5'))
max=int(N.replace('5','6'))+int(M.replace('5','6'))
print(min, max)
"""

#1541 잃어버린 괄호--> 문제 이해를 잘못 수행
#이 문제의 경우 '+'가 가장 먼저 수행되어야 한다
"""
N=input().split('-')
count=0
sub=[]
for i in N:
    if '+' in i:
        num=i.split('+')
        for j in num:
            count+=int(j)
for i in N:
    if '+' not in i:
        sub.append(i)
        for j in sub:
            count=j-count
"""
#BOJ1541 잃어버린 괄호 (o)
"""
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
"""

#