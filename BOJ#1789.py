S=int(input())
ls=[]
for i in range(1,S+1):
    if S>i and S-i>=i+1:
        ls.append(i)
        S-=i
        i+=1
    elif S==i:
        ls.append(i)
        break
print(len(ls))