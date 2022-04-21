import sys
input = sys.stdin.readline
N = int(input())
ls=[]
for i in range(N):
    word = str(input().rstrip())
    if word in ls:
        pass
    else:
        ls.append(word)
ls.sort()
ls.sort(key = lambda x : len(x))
for i in ls:
    print(i)