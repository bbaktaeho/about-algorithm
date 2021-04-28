import sys; input = sys.stdin.readline
from collections import deque

def bfs(weight):
    q = deque([s_island])
    visited = [False] * (N + 1)
    visited[s_island] = True
    while q:
        island = q.popleft()
        for y, w in country[island]:
            if not visited[y] and w >= weight: 
                visited[y] = True
                q.append(y)
    return visited[e_island]

start_w = 1000000000
end_w = 1

N, M = map(int, input().split())
country = [[] for _ in range(N+1)]
for _ in range(M):
    x, y, w = map(int, input().split())
    country[x].append((y, w))
    country[y].append((x, w))
    start_w = min(start_w, w)
    end_w = max(end_w, w)

s_island, e_island = map(int, input().split())
result = start_w
while start_w <= end_w:
    mid_w = (start_w + end_w) // 2
    if bfs(mid_w):
        result = mid_w
        start_w = mid_w + 1
    else: end_w = mid_w - 1
print(result)