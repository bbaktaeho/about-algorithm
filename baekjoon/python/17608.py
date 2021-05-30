import sys; input = sys.stdin.readline

N = int(input())
stack = []
for i in range(N):
    stack.append(int(input()))

count = 1
number = stack.pop()
while stack:
    temp_number = stack.pop()
    if number < temp_number:
        count += 1
        number = temp_number

print(count)
