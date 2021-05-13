import sys; input = sys.stdin.readline

AN, BN = map(int, input().split())
result = {i: 0 for i in input().split()}

for i in input().split():
    if i in result: result.pop(i)

print(len(result))
print(*sorted(map(int, result.keys())))

