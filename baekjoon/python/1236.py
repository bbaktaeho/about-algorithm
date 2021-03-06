import sys; input = sys.stdin.readline

# N, M = map(int, input().strip().split())
# board = []
# for _ in range(N): board.append(list(input().strip()))
# result = 0 # 최소로 추가하는 경비 수

# def column_check(c):
#     for r in range(N):
#         if board[r][c] == 'X': return True
#     return False

# for i in range(N): # 로우 
#     if board[i].count('X') == 0: # ....
#         pre_result = result
#         for j in range(M):
#             if not column_check(j): 
#                 board[i][j] = 'X'
#                 result += 1
#                 break
#         if pre_result == result: result += 1 # 아무곳에 경비를 둠

# for i in range(M): # 컬럼
#     if not column_check(i): result += 1

# print(result)

N, M = map(int, input().split())
castle = []
for _ in range(N): castle.append(input().rstrip())

rows = [0] * N
cols = [0] * M

for i in range(N):
    for j in range(M):
        if castle[i][j] == 'X':
            rows[i] = 1
            cols[j] = 1

print(max(rows.count(0), cols.count(0)))