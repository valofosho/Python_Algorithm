from collections import deque

v, e = map(int, input().split())
# 진입차수 초기화
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int,input().split())
    graph[a].append(b)
    # 진입차수 1 증가
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            # 연결된 노드들의 진입차수에서 1 빼주기
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end= ' ')
topology_sort()