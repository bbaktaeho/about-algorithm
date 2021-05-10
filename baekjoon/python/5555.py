import sys; input = sys.stdin.readline

search = input().rstrip()
count = 0
for _ in range(int(input())):
    s = input().rstrip() * 2
    if s != s.replace(search, ""): count += 1

print(count)