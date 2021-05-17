import sys
sys.setrecursionlimit(100000)
min_value = sys.maxsize
count = 0

def solution(r, c):
    x = [1, 0]
    y = [0, 1]
    ch = [[0 for _ in range(r+1)] for _ in range(c+1)]

    def dfs(xx, yy, dis):
        global min_value, count
        if xx == c and yy == r:
            if min_value < dis: return
            elif min_value > dis: 
                min_value = dis
                count = 1
            else: count += 1
        else:
            for i in range(2):
                dx = xx + x[i]
                dy = yy + y[i]
                if ch[xx][yy] == 0 and 0 < dx <= c and 0 < dy <= r:
                    ch[xx][yy] = 1
                    dfs(dx, dy, dis+1)
                    ch[xx][yy] = 0
    
    dfs(1,1,0)
    return count

