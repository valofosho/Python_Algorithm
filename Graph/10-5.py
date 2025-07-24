# 크루스칼 알고리즘

# find
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]
# union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i


for i in range(e):
    a, b, cost = map(int,input().split())
    edges.append((cost, a, b))
# 간선 오름차순 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)
