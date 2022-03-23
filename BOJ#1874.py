import sys
input = sys.stdin.readline
N = int(input())
s, t, f = [], [], []
for i in range(N):
    a=int(input())
    s.append(a)
comp=1
error_code=0
for idx in range(N):
    while comp <= s[idx]:
        t.append(comp)
        f.append("+")
        comp+=1
    if t[-1] == s[idx]:
        t.pop()
        f.append("-")
    else:
        print("NO")
        error_code=1
        break
if not error_code == 1:
    print('\n'.join(f))
