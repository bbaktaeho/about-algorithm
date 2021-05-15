from collections import deque

def bfs(x, y):
    visited = [[0] * M for _ in range(N+1)] 
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == N-1 and y == M-1: return visited[N-1][M-1]
        for next_x, next_y in [(x, y+1), (x+1, y), (x-1, y), (x, y-1)]:
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M: continue
            if visited[next_x][next_y] or board[next_x][next_y] != 1: continue
            q.append((next_x, next_y))
            visited[next_x][next_y] = visited[x][y] + 1

N, M = map(int, input().split())
board = []
for _ in range(N): board.append(list(map(int, list(input()))))

print(bfs(0, 0))