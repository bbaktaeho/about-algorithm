# import sys; input = sys.stdin.readline
# from collections import deque

# N = int(input())

# graph = [[] for _ in range(N+1)]
# result = 0

# def dfs(v):
#     global result
#     if visited[v]: return
#     visited[v] = True
#     result += 1
#     for next_v in graph[v]: dfs(next_v)

# def bfs(v):
#     count = 0
#     q = deque([v])
#     while q:
#         com = q.popleft()
#         if visited[com]: continue
#         visited[com] = True
#         count += 1
#         for next_com in graph[com]: q.append(next_com)
#     return count

# for _ in range(int(input())):
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph[y].append(x)

# # visited = [False] * (N + 1)
# # dfs(1)
# # print(result - 1)
# visited = [False] * (N + 1)
# print(bfs(1) - 1)

def dfs(v):
    global count
    if visited[v]: return
    visited[v] = True
    count += 1
    for com in networks[v]: dfs(com)

import sys; input = sys.stdin.readline
n = int(input())
networks = [[] for _ in range(n+1)] 
visited = [False] * (n+1) 

count = -1

for _ in range(int(input())):
    x, y = map(int, input().split())
    networks[x].append(y)
    networks[y].append(x)

dfs(1)
print(count)