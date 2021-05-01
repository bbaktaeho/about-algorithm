import sys; input = sys.stdin.readline
N = int(input())
rank_list = sorted([int(input()) for _ in range(N)])
result = 0
for r in range(1, N+1):
    if r != rank_list[r-1]: 
        result += abs(rank_list[r-1] - r)
print(result)