# import sys
# sys.setrecursionlimit(10**6)
# rl = sys.stdin.readline
# def dfs(x, y):
#     if x < 0 or x >= n or y < 0 or y >= m:
#         return
#     if not board[x][y] or visited[x][y]:
#         return
#     visited[x][y] = True
#     dfs(x-1, y)
#     dfs(x+1, y)
#     dfs(x, y-1)
#     dfs(x, y+1)

# for _ in range(int(rl())):
#     m, n, k = map(int, rl().split())
#     board = [[0] * m for _ in range(n)]

#     for _ in range(k):
#         y, x = map(int, rl().split())
#         board[x][y] = 1
    
#     visited = [[False] * m for _ in range(n)]
#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if board[i][j] == 1 and not visited[i][j]:
#                 dfs(i, j)
#                 cnt += 1
#     print(cnt)

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def dfs(x, y):
#     if x < 0 or x >= N or y < 0 or y >= M: return
#     if board[x][y] == 0 or visited[x][y]: return
#     visited[x][y] = True
#     dfs(x-1, y)
#     dfs(x+1, y)
#     dfs(x, y-1)
#     dfs(x, y+1)

# for _ in range(int(input())):
#     M, N, K = map(int, input().split())
#     board = [[0] * M for _ in range(N)]
#     visited = [[False] * M for _ in range(N)]
#     cnt = 0

#     for _ in range(K):
#         y, x = map(int, input().split())
#         board[x][y] = 1

#     for i in range(N):
#         for j in range(M):
#             if board[i][j] and not visited[i][j]: 
#                 dfs(i, j)
#                 cnt += 1
    
#     print(cnt)

def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N: return
    if visited[x][y] or board[x][y] == 0: return
    visited[x][y] = True
    for new_x, new_y in [(x-1, y), (x+1, y), (x, y-1), (x,y+1)]:
        dfs(new_x, new_y)

def bfs(v1, v2):
    q = deque([(v1, v2)])
    visited[v1][v2] = True
    while q:
        x, y = q.popleft()
        for next_x, next_y in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N: continue
            if visited[next_x][next_y] or board[x][y] != 1: continue
            q.append((next_x, next_y))
            visited[next_x][next_y] = True

import sys; input = sys.stdin.readline; sys.setrecursionlimit(100000)
from collections import deque

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    board = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        board[x][y] = 1
    
    result = 0
    for i in range(M):
        for j in range(N):
            if not visited[i][j] and board[i][j] != 0:
                bfs(i, j)
                result += 1
    
    print(result)