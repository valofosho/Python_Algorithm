n, k = map(int,input().split())
answer = 0
imsi = (n//k) * k
ones = n-imsi
answer += ones
while True:
    if imsi == 1:
        break
    answer += 1
    imsi //= k
print(answer)