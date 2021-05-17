import sys
sys.setrecursionlimit(100000)
Min = sys.maxsize
cnt = 0

# 시간 초과는 뭘까요!!

def solution(r, c):
    x = [1, 0]
    y = [0, 1]
    def DFS(xx, yy):
        global cnt
        if xx == c and yy == r:
            cnt += 1
        else:
            for i in range(2):
                dx = xx + x[i]
                dy = yy + y[i]
                if dx <= c and dy <= r: DFS(dx, dy)
                    
    DFS(1, 1)
    return cnt


print(solution(5,5))