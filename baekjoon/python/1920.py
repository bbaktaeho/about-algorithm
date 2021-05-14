# 1
# N, arr1, M, arr2 = (int(input()), input().split(), int(input()), input().split())
# arr1 = set(arr1)

# for i in arr2:
#     if i in arr1:
#         print(1)
#     else:
#         print(0)

# N, arr1, M, arr2 = (int(input()), {i: 1 for i in map(int, input().split())}, int(input()), input().split())
# for i in list(map(int, arr2)):
#     print(arr1.get(i, 0))

# def bs(f, N):
#     start, mid, end = 0, 0, N-1
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] < f: start = mid + 1
#         elif arr[mid] > f: end = mid - 1
#         else: return 1
#     return 0

# N = int(input())
# arr = sorted(list(map(int, input().split())))
# M = int(input())
# f_arr = list(map(int, input().split()))
# for f in f_arr: print(bs(f, N))

# 2
# import sys; input = sys.stdin.readline
# N = int(input())
# N_arr = sorted(map(int, input().split()))
# M = int(input())
# M_arr = list(map(int, input().split()))

# def bs(num):
#     start, end = 0, N-1
#     while start <= end:
#         mid = (start + end) // 2
#         if num == N_arr[mid]: return 1
#         elif num < N_arr[mid]: end = mid - 1
#         else: start = mid + 1
#     return 0

# for m in M_arr: print(bs(m))

N = int(input())
n_arr = sorted((map(int, input().split())))
M = int(input())
m_arr = map(int, input().split())

result = []

for m in m_arr:
    start, end = 0, N-1
    result_len = len(result)
    while start <= end:
        mid = (start + end) // 2
        if n_arr[mid] == m: 
            result.append(1)
            break
        elif n_arr[mid] < m: start = mid+1
        else: end = mid-1
    if result_len == len(result): result.append(0)

print(*result, sep='\n')