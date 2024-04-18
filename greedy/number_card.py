n, m = map(int, input().split())
answer = 0
for i in range(n):
    data = list(map(int, input().split()))
    print(data)
    min_num = min(data)
    answer =  max(answer, min_num)
print(answer)