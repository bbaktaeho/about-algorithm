from collections import deque

N = int(input())
balloon_list = [(i+1, v) for i,v in enumerate(map(int, input().split()))]
q = deque(balloon_list)

result = [1]
start = 0
node = q.popleft()
while q:
    if node[1] > 0:
        for _ in range(node[1]-1): q.append(q.popleft())
        start = 1
    else:
        for _ in range(abs(node[1])-1): q.appendleft(q.pop())
        start = -1
    node = q.popleft() if start > 0 else q.pop()
    result.append(node[0])

print(*result)