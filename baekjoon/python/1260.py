# from sys import stdin
# from collections import deque
# input = stdin.readline

# N, M, V = map(int, input().split())
# v_arr = [[] for _ in range(N+1)]
# for _ in range(M):
#     x, y = map(int, input().split())
#     v_arr[x].append(y)
#     v_arr[y].append(x)

# for arr in v_arr: arr.sort()

# dfs_result = []
# bfs_result = []
# visited = [False] * (N + 1)

# def dfs(v):
#     if visited[v]: return
#     dfs_result.append(v)
#     visited[v] = True
#     for next_v in v_arr[v]: dfs(next_v)

# def bfs(v):
#     q = deque([v])
#     while q:
#         cur = q.popleft()
#         if visited[cur]: continue
#         bfs_result.append(cur)
#         visited[cur] = True
#         for next_v in v_arr[cur]: q.append(next_v)

# dfs(V)
# visited = [False] * (N + 1)
# bfs(V)
# print(*dfs_result)
# print(*bfs_result)


import sys; input = sys.stdin.readline
from collections import deque

def dfs(v):
    if visited[v]: return
    visited[v] = True
    dfs_result.append(v)
    for next_v in graph[v]: dfs(next_v)

def bfs(v):
    q = deque([v])
    while q:
        cur_v = q.popleft()
        if visited[cur_v]: continue
        visited[cur_v] = True
        bfs_result.append(cur_v)
        for next_v in graph[cur_v]:
            if not visited[next_v]: q.append(next_v)


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
dfs_result = []
bfs_result = []

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for g in graph: g.sort()

visited = [False] * (N+1)
dfs(V)
visited = [False] * (N+1)
bfs(V)
print(*dfs_result)
print(*bfs_result)