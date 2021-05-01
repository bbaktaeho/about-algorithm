import sys; input = sys.stdin.readline
import heapq

q = []
for _ in range(int(input())): heapq.heappush(q, int(input()))

result = 0
while len(q) != 1:
    v = heapq.heappop(q) + heapq.heappop(q)
    result += v
    heapq.heappush(q, v)
print(result)