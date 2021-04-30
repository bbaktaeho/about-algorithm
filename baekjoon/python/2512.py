import sys; input = sys.stdin.readline
N = int(input())
budget_list = sorted(list(map(int, input().split())))
M = int(input())

def is_possible(limit):
    total = M
    for budget in budget_list:
        if total < 0: return False
        total -= (budget if budget <= limit else limit)
    return True if total >= 0 else False

start, end = 1, budget_list[-1]
while start <= end:
    mid = (start + end) // 2
    if is_possible(mid): start = mid + 1
    else: end = mid - 1
print(end)