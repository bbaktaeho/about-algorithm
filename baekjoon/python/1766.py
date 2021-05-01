import sys; input = sys.stdin.readline
import heapq

q = []
N, M = map(int, input().split())
relation_list = [[] for _ in range(N+1)]
degree_list = [0] * (N+1)
result = []

for _ in range(M):
    x, y = map(int, input().split())
    relation_list[x].append(y)
    degree_list[y] += 1

for i in range(1, N+1):
    if degree_list[i] == 0: heapq.heappush(q, i)

while q:
    node = heapq.heappop(q)
    result.append(node)
    for n in relation_list[node]:
        degree_list[n] -= 1
        if degree_list[n] == 0: heapq.heappush(q, n)

print(*result)