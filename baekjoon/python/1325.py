# import sys; input = sys.stdin.readline
# from collections import deque
# sys.setrecursionlimit(10 ** 6)

# def bfs(v):
#     q = deque([v])
#     visited = [False] * (N+1)
#     visited[v] = True
#     count = 1
#     while q:
#         cur_v = q.popleft()
#         for next_v in computers[cur_v]:
#             if not visited[next_v]:
#                 visited[next_v] = True
#                 q.append(next_v)
#                 count += 1
#     return count

# def dfs(v):
#     global dfs_count
#     if dfs_visited[v]: return
#     dfs_visited[v] = True
#     dfs_count += 1
#     for next_v in computers[v]: dfs(next_v)

            
# N, M = map(int, input().split())
# dfs_count = 0
# computers = [[] for _ in range(N+1)]
# for _ in range(M):
#     A, B = map(int, input().split())
#     computers[B].append(A)

# result = []
# max_result = 0
# for com in range(1, N+1): 
#     dfs_visited = [False] * (N + 1)
#     dfs_count = 0
#     dfs(com)
#     # virus_count = bfs(com)
    
#     if not result or max_result == dfs_count: 
#         max_result = dfs_count
#         result.append(com)
#     elif max_result < dfs_count: 
#         result = [com]
#         max_result = dfs_count
# print(*sorted(result))

def dfs(c):
    global hack_count
    hack_count += 1
    for next_c in trust[c]:
        if not visited[next_c]: 
            visited[next_c] = True
            dfs(next_c)

def bfs(c):
    visited = [False] * (N+1)
    hack_count = 0
    q = deque([c])
    visited[c] = True
    while q:
        cur = q.popleft()
        hack_count += 1
        for next_c in trust[cur]:
            if not visited[next_c]: 
                q.append(next_c)
                visited[next_c] = True
    return hack_count

import sys; sys.setrecursionlimit(100000)
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
trust = [[] for _ in range(N+1)]
result = []
for _ in range(M):
    x, y = map(int, input().split())
    trust[y].append(x)

max_count = 0
for i in range(1, N+1):
    # hack_count = 0
    # visited = [False] * (N+1)
    # dfs(i)
    hack_count = bfs(i)
    if max_count == hack_count: result.append(i)
    elif hack_count > max_count: 
        result = [i]
        max_count = hack_count

print(*sorted(result))
