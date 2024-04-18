from collections import deque
n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
visited = [[0]*m for _ in range(n)]
# 1이 길 # 0이 벽
def in_range(x,y):
    return 0<=x<n and 0<=y<m
def bfs(x, y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in (-1,0), (1,0), (0,-1), (0,1):
            nx, ny = x+i[0], y+i[1]
            if in_range(nx,ny):
                if graph[nx][ny] == 0:
                    continue
                else:
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        graph[nx][ny] = graph[x][y] +1
                        q.append((nx,ny))
    return graph[n-1][m-1]
print(bfs(0,0))
"""
input
5 6
101010
111111
000001
111111
111111

"""