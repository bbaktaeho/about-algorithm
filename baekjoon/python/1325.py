import sys; input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10 ** 6)

def bfs(v):
    q = deque([v])
    visited = [False] * (N+1)
    visited[v] = True
    count = 1
    while q:
        cur_v = q.popleft()
        for next_v in computers[cur_v]:
            if not visited[next_v]:
                visited[next_v] = True
                q.append(next_v)
                count += 1
    return count

def dfs(v):
    global dfs_count
    if dfs_visited[v]: return
    dfs_visited[v] = True
    dfs_count += 1
    for next_v in computers[v]: dfs(next_v)

            
N, M = map(int, input().split())
dfs_count = 0
computers = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    computers[B].append(A)

result = []
max_result = 0
for com in range(1, N+1): 
    dfs_visited = [False] * (N + 1)
    dfs_count = 0
    dfs(com)
    # virus_count = bfs(com)
    
    if not result or max_result == dfs_count: 
        max_result = dfs_count
        result.append(com)
    elif max_result < dfs_count: 
        result = [com]
        max_result = dfs_count
print(*sorted(result))