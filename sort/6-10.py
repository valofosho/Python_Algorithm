n = int(input())
arr = [
    int(input())
    for _ in range(n)
]
arr = sorted(arr, reverse = True)

for i in arr:
    print(i, end=' ')