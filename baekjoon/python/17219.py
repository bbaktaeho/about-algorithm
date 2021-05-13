import sys; input = sys.stdin.readline

N, M = map(int, input().split())

site_dict = {}

for _ in range(N): # 사이트 주소와 비밀번호
    site, pw = input().split()
    site_dict[site] = pw

for _ in range(M):
    print(site_dict[input().rstrip()])