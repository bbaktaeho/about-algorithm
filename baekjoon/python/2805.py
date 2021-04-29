import sys; input = sys.stdin.readline

def is_slice(h):
    total = 0
    for tree in tree_list:
        slice = tree - h
        total += (slice if slice > 0 else 0)
    return True if total >= M else False

N, M = map(int, input().split())
tree_list = list(map(int, input().split()))
tree_list.sort()

start, end = 0, 2000000000
while start <= end:
    mid = (start + end) // 2
    if is_slice(mid): start = mid + 1
    else: end = mid - 1
print(end)
