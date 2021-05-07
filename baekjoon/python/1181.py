import sys; input = sys.stdin.readline

arr = set()
for _ in range(int(input())):
    arr.add(input().rstrip())

for word in sorted(arr, key=lambda x: (len(x), x)): print(word)