# 기본적인 서로소 집합 알고리즘 소스코드
# 특정 원소 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    a, b = map(int,input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합:', end = ' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end = ' ')

print('부모 테이블:', end = ' ')
for i in range(1, v+1):
    print(parent[i], end=' ')