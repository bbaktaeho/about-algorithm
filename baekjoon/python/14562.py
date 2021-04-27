import sys; input = sys.stdin.readline
from collections import deque

def bfs(s, t):
    q = deque([(0, s, t)])
    while q:
        cur = q.popleft()
        if cur[1] == cur[2]: return cur[0]
        if cur[1]*2 <= cur[2]+3: q.append((cur[0]+1, cur[1]*2, cur[2]+3))
        q.append((cur[0]+1, cur[1]+1, cur[2]))

for _ in range(int(input())):
    S, T = map(int, input().split())
    print(bfs(S, T))