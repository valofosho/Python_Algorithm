#1439 (뒤집기)
N=list(map(str,input()))
count=0
for _ in range(len(N)-1):
    if N[_]!=N[_+1]:
        count+=1
count=(count+1)//2
print(count)
