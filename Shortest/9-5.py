import heapq
import sys

INF = int(1e9)

n, m, start =map(int,input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int,input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)

count = 0
# 도달할 수 있는 노드 중, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    if d!= INF:
        count +=1 
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count -1
print(count-1, max_distance)