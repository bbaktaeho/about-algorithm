# N = int(input())

# def binarySearch(N):
#     start, mid, end = 1, 0, N // 2
#     while start <= end:
#         mid = (start + end) // 2
#         result = mid * mid
#         if result > N: end = mid - 1
#         elif result < N: start = mid + 1
#         else: break
#     return mid

# print(binarySearch(N))

N = int(input())
start, end = 0, N // 2
mid = start
while start <= end:
    mid = (start + end) // 2
    result = mid**2
    if N < result: end = mid - 1
    elif N > result: start = mid + 1
    else: break
print(mid+1 if mid**2 < N else mid)