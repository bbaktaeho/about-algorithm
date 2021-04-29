import sys; input = sys.stdin.readline

def bs(num):
    result = -1
    start, end = 0, N-1
    while start <= end:
        mid = (start + end) // 2
        if B[mid] == num: 
            result = mid
            end = mid - 1
        elif B[mid] < num: start = mid + 1
        else: end = mid - 1
    return result

N, M = map(int, input().split())
A = []
for _ in range(N): A.append(int(input()))
B = sorted(A)
for _ in range(M): print(bs(int(input())))
