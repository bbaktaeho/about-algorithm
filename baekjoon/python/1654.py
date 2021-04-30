import sys; input = sys.stdin.readline
K, N = map(int, input().split())
lan_list = sorted([int(input()) for _ in range(K)])

def is_slice(cm):
    total = 0
    for lan in lan_list:
        if total >= N: break
        total += lan // cm
    return True if total >= N else False

start, end = 0, lan_list[-1]
while start <= end:
    mid = (start + end) // 2
    if mid == 0: break
    if (is_slice(mid)): start = mid + 1
    else: end = mid - 1
print(end)
