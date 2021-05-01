import sys; input = sys.stdin.readline

N, K = map(int, input().split())
arr = [0] * (K+1)

for _ in range(N):
    W, V = map(int, input().split())
    for i in range(W, K+1):
        arr[i] = max(arr[i], V + arr[i-W])
print(arr[-1])



import sys; input = sys.stdin.readline

N, K = map(int, input().split())
arr = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    W, V = map(int, input().split())
    for j in range(1, K+1):
        if j < W: arr[i][j] = arr[i-1][j]
        else: arr[i][j] = max(arr[i-1][j], arr[i-1][j-W] + V)
print(arr[N][K])