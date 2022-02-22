#BOJ5585 (거스름돈)
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