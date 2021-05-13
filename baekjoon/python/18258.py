import sys; input = sys.stdin.readline
from collections import deque

q = deque()
result = []

for _ in range(int(input())):
    command = input().split()
    
    if command[0] == "push": 
        q.append(command[1])
    elif command[0] == "pop": 
        print(q.popleft() if q else -1)
    elif command[0] == "size": 
        print(len(q))
    elif command[0] == "empty": 
        print(0 if q else 1) 
    elif command[0] == "front":
        print(q[0] if q else -1)
    elif command[0] == "back": 
        print(q[-1] if q else -1)

# print("\n".join(map(str, result)))