import sys; input = sys.stdin.readline

arr = []
for _ in range(int(input())): arr.append(input().rstrip())
arr.sort()

def min_sum(s):
    total = 0
    for c in s:
        if c.isdigit(): total += int(c)
    return total

arr.sort(key=lambda x: (len(x), min_sum(x)))
print("\n".join(arr))