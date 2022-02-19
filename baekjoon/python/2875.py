import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

N_share, N_rem = divmod(N, 2)
