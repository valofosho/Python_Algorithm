# n, m = list(map(int,input().split(' ')))
# array = list(map(int, input().split()))
# start = 0
# end = max(array)
# while start <= end:
#     temp = 0
#     mid = (start + end) // 2
#     for i in array:
#         if i > mid:
#             temp += i-mid
#     if temp < m:
#         end = mid -1
#     else:
#         result = mid
#         start = mid + 1
# print(result)

# def binary(arr, target, start, end,ans):
#     temp = 0
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     for i in arr:
#         if i > mid:
#             temp += i - mid
#     if temp < m:
#         return binary(arr, target, start, mid + 1,ans)
#     else:
#         ans.append(mid)
#         if mid-1 <= end:
#             return binary(arr, target, mid-1, end,ans)
#         else:
#             return None

# n, m = list(map(int,input().split(' ')))
# array = list(map(int, input().split()))
# start = 0
# end = max(array)
# ans = []
# binary(array, m, start, end,ans)
# print(ans)

"""
입력
4 6
19 15 10 17
출력
15
"""

def binary(arr, target, start, end, ans):
    if start > end:
        return None
    mid = (start + end) // 2
    temp = 0
    for i in arr:
        if i > mid:
            temp += i - mid
    if temp < target:
        return binary(arr, target, start, mid - 1, ans)
    else:
        ans[0] = mid
        return binary(arr, target, mid + 1, end, ans)
n, m = list(map(int, input().split()))
array = list(map(int, input().split()))
start = 0
end = max(array)
ans = [0]
binary(array, m, start, end, ans)
print(ans[0])
