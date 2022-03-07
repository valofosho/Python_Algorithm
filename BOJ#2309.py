ls=[]
ans=100
total=0
for i in range(9):
    ls.append(int(input()))
total=sum(ls)
for i in range(9):
    for j in range(i+1,9):
        if ans== total-(ls[i] + ls[j]):
            num1, num2= ls[i], ls[j]
            ls.remove(num1)
            ls.remove(num2)
            ls.sort()
            for _ in range(len(ls)):
                print(ls[_])
            break
    if len(ls)<9:
        break