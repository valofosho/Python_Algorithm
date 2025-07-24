def binary_re(array, target, start, end):
    if start > end:
        return 'no'
    mid = (start + end) // 2
    if array[mid] == target:
        return 'yes'
    elif array[mid] < target:
        return binary_re(array, target, mid + 1, end)
    else:
        return binary_re(array, target, start, mid -1)

def binary_for(array, target, start, end):
    while start<= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 'yes'
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 'no'

n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
inquire = list(map(int, input().split()))
for i in range(len(inquire)):
    ans = binary_for(array, inquire[i], 0, n-1)
    print(ans, end = ' ')
"""
입력 예시
5
8 3 7 9 2
3
5 7 9
"""