# # def isSame(arr, N):
# #     for i in range(N - 1):
# #         if arr[i] != arr[i + 1]:
# #             return False
# #     return True

# def isSame(arr):
#     if len(set(arr)) == 1:
#         return True
#     return False


# T = int(input())
# while T:
#     N = int(input())
#     arrC = list(map(int, input().split()))

#     count = 0
#     while True:
#         for i in range(N):
#             if arrC[i] % 2 != 0:
#                 arrC[i] += 1
#         if isSame(arrC):
#             break
#         arrPlus = list(map(lambda x: x // 2, arrC))
#         for i in range(N):
#             arrC[i] -= arrPlus[i]
#         arrC[0] += arrPlus[N - 1]
#         for i in range(N - 1):
#             arrC[i + 1] += arrPlus[i]
#         count += 1
#     print(count)
#     T -= 1


# 홀수개의 사탕을 가지게 된 아이가 있을 경우 
# 선생님이 한 개를 보충해 짝수로 만들어 주기

def sum_one(x):
    return x + (1 if x % 2 == 1 else 0)

def divide_two(x):
    return x // 2

for _ in range(int(input())):
    n = int(input())
    count = 0
    candy_list = list(map(int, input().split()))

    while 1:
        candy_list = list(map(sum_one, candy_list))
        if len(set(candy_list)) == 1: break
        sum_candy_list = list(map(divide_two, candy_list))
        for i in range(-1, n-1): candy_list[i+1] = sum_candy_list[i+1] + sum_candy_list[i] 
        count += 1
    print(count)
