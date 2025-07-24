n = int(input())
arr = []
for _ in range(n):
    a = input().split()
    arr.append([a[0],int(a[1])])

arr = sorted(arr, key = lambda x: x[1])
for i in arr:
    print(i[0], end = ' ')