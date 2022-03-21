cnt=0
stack=[]
N=int(input())
for i in range(N):
    x=int(input())
    if x==0:
        stack.pop()
    else:
        stack.append(x)
for j in range(len(stack)):
    cnt += stack[j]
print(cnt)