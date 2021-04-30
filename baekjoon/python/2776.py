import sys; input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    dict_1 = {}
    for n in map(int, input().split()):
        if not dict_1.get(n): dict_1[n] = 1
    M = int(input())
    for m in map(int, input().split()):
        if dict_1.get(m): print(1)
        else: print(0)