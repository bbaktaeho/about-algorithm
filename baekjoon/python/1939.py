import sys; input = sys.stdin.readline
from collections import deque

# def bfs(weight):
#     q = deque([s_island])
#     visited = [False] * (N + 1)
#     visited[s_island] = True
#     while q:
#         island = q.popleft()
#         for y, w in country[island]:
#             if not visited[y] and w >= weight: 
#                 visited[y] = True
#                 q.append(y)
#     return visited[e_island]

# start_w = 1000000000
# end_w = 1

# N, M = map(int, input().split())
# country = [[] for _ in range(N+1)]
# for _ in range(M):
#     x, y, w = map(int, input().split())
#     country[x].append((y, w))
#     country[y].append((x, w))
#     start_w = min(start_w, w)
#     end_w = max(end_w, w)

# s_island, e_island = map(int, input().split())
# result = start_w
# while start_w <= end_w:
#     mid_w = (start_w + end_w) // 2
#     if bfs(mid_w):
#         result = mid_w
#         start_w = mid_w + 1
#     else: end_w = mid_w - 1
# print(result)

def bfs(weight):
    visited = [False] * (N + 1)
    visited[start] = True
    q = deque([start])
    while q:
        node = q.popleft()
        for y, w in node_list[node]:
            if not visited[y] and weight <= w:
                visited[y] = True
                q.append(y)
    return visited[end]        

N, M = map(int, input().split())
node_list = [[] for _ in range(N+1)]
min_w, max_w = 1000000000, 1
for _ in range(M):
    x, y, w = map(int, input().split())
    node_list[x].append((y, w))
    node_list[y].append((x, w))
    min_w = min(min_w, w)
    max_w = max(max_w, w)

result = min_w
start, end = map(int, input().split())
while min_w <= max_w:
    mid_w = (max_w + min_w) // 2
    if bfs(mid_w):
        min_w = mid_w + 1
        result = mid_w
    else: max_w = mid_w - 1

print(result)