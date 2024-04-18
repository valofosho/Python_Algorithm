n, m = map(int,input().split())
visited =[[0]*m for _ in range(n)]
# 현재 위치에서 왼쪽 방향(반시계 90도 회전)
# visited = 0 이면 회전 후 전진, 1이면 회전만 진행
# 모두 visited = 1이거나 바다면 방향을 유지한채 back
# 뒤쪽이 바다이면 움직임 멈춤
# 0 - UP
# 1 - RIGHT
# 2 - DOWN
# 3 - LEFT
x, y, direction = map(int, input().split())
array = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited[x][y] = 1


dxs = [0, 1, 0, -1]
dys = [-1, 0, 1, 0]

# dxy[0] - 0(북)
# dxy[1] - 1(동)
# dxy[1] - 2(남)
# dxy[2] - 3(서)


def is_range(x, y):
    return 0<=x<n and 0<=y<m
def is_visited(x,y):
    return visited[x][y]
def check_sea(x,y):
    return array[x][y]

def change_direction(direction):
    if direction -1 <0:
        direction = 3
    else:
        direction -= 1
    return direction
def move(x, y, direction, turned):
    new_direct = change_direction(direction)
    dx, dy = x + dxs[new_direct], y + dys[new_direct]
    # 갈 수 있고, 방문하지 않았을 경우
    if is_range(dx, dy) and is_visited(dx,dy) == 0:
        # 바다가 아니면 간다
        if check_sea(dx, dy) == 0:
            print(x,y)
            x, y = dx, dy
            visited[x][y] = 1
            turned = 0
        # 바다면 못가요
        else:
            print(x,y,new_direct)
            turned += 1
    return x, y, new_direct, turned

def backward(x, y, direction, turned):
    dx, dy = x-dxs[direction], y-dys[direction]
    if array[dx][dy] == 0:
        x, y = dx, dy
        visited[x][y] = 1
        turned = 0
    return x, y, direction, turned

turned = 0
while turned != 4:
    x, y, direction, turned = move(x,y,direction,turned)
    if turned == 4:
        x, y, direction, turned = backward(x, y, direction, turned)
print(visited)
count = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 1:
            count += 1
print(count)


"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1    
"""