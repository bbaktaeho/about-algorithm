import math
X, Y = map(int, input().split())
Z = math.floor(100 * Y / X)

def is_change(game):
    z = math.floor(100 * (Y + game) / (X + game))
    return True if Z < z else False

start, end = 0, 1000000000
while start <= end:
    mid = (start + end) // 2
    if is_change(mid): end = mid - 1
    else: start = mid + 1

print(start if is_change(start) else -1)