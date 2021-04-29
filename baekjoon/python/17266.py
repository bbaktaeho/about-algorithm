# import math
# import sys
# input = sys.stdin.readline
# N = int(input())
# M = int(input())
# x_arr = list(map(int, input().split()))

# gap = []
# if len(x_arr) > 1:
#     for i in range(M-1): gap.append(x_arr[i+1] - x_arr[i])
#     max_gap = math.ceil(max(gap) / 2) # 가로등 사이의 최대 차이를 이용하여 최소 높이를 찾음
#     print(max(max_gap, x_arr[0], N - x_arr[-1]))
# else:
#     print(max(x_arr[0], N - x_arr[-1]))

import sys; input = sys.stdin.readline
N = int(input()) # 5
M = int(input()) # 2
street_list = list(range(N))
lamp_list = list(map(int, input().split()))

start, end = 1, N
result = start
while start <= end:
    mid = (start + end) // 2
    flag = True
    for i in range(M - 1):
        right = lamp_list[i] + mid
        if right < lamp_list[i+1] - mid: 
            flag = False
            break
    if lamp_list[0] - mid > 0: flag = False
    if lamp_list[-1] + mid < N: flag = False
    if flag:
        result = mid
        end = mid - 1
    else: start = mid + 1
print(result)

