N = int(input())
data = list(map(str, input().split()))

def is_range(x, y):
    return 1<=x<=N and 1<=y<=N

x, y = 1, 1
dxs = [-1,1,0,0]
dys = [0,0,-1,1]
moves = ["L","R","U","D"]
for i in data:
    idx = moves.index(i)
    dx = x + dxs[idx]
    dy = y + dys[idx]
    if is_range(dx, dy):
        x, y = dx, dy
    print(idx, x, y)
print(y, x)