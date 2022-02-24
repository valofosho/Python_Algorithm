#BOJ1931 (회의실 배정)
#TIL: sort 메소드는 인자를 여러개로 활용 가능하며, 우선순위는 할당 순서에 비례한다.
N=int(input())
lst=[]
ans=[]
for i in range(N):
    lst.append(list(map(int,input().split())))
lst.sort(key=lambda x: (x[1],x[0]))
for i in range(len(lst)-1):
    if lst[i][0]<=lst[i+1][0]:
        print("오늘은 여기까지 머리아프다")

print(lst)
