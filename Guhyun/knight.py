place = input()
garo = int(place[1])
sero = int(ord(place[0])) - int(ord('a')) + 1
answer = 0
dxs = [-2, -2, -1, -1, 1, 1, 2, 2]
dys = [-1, 1, -2, 2, -2, 2, -1, 1]

def is_range(x,y):
    return 1<=x<=8 and 1<=y<=8

for i in range(8):
    dx, dy = garo + dxs[i], sero + dys[i]
    if is_range(dx, dy):
        answer += 1
print(answer)