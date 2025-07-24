def find_team(parent, x):
    if parent[x] != x:
        parent[x] = find_team(parent, parent[x])
    return parent[x]
def union(parent, a, b):
    a = find_team(parent, a)
    b = find_team(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int,input().split())
parent = [0] * (v+1)

for i in range(0, v+1):
    parent[i] = i

for i in range(e):
    inst, a ,b = map(int,input().split())
    if inst == 0:
        union(parent, a, b)
    elif inst == 1:
        if find_team(parent,a) == find_team(parent, b):
            print("YES")
        else:
            print("NO")


"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
0 1 1
"""