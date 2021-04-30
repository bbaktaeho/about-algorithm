import sys; input = sys.stdin.readline

S = set()

def sol(cal, x = -1):
    global S
    if cal == 'all': S = set(range(1, 21))
    elif cal == 'empty': S.clear()
    elif cal == 'add': S.add(x)
    elif cal == 'remove': S.remove(x) if x in S else None
    elif cal == 'check': print(1 if x in S else 0)
    elif cal == 'toggle': S.remove(x) if x in S else S.add(x)

for _ in range(int(input())):
    cal = input().split()
    if len(cal) == 1: sol(cal[0])
    else: sol(cal[0], int(cal[1]))