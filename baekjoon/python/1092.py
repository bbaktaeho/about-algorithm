import sys; input = sys.stdin.readline

N = int(input()) # 크레인의 수
crane_list = sorted(map(int, input().split()), reverse=True)
M = int(input()) # 박스의 수
box_list = sorted(map(int, input().split()),  reverse=True)
loaded_list = [False] * M

def sol():
    time = 0
    count = 0
    start = 0
    if crane_list[0] < box_list[0]: return -1
    while count != len(box_list):
        for crane in crane_list:
            for i in range(start, M):
                if loaded_list[i]: continue
                if box_list[i] <= crane:
                    loaded_list[i] = True
                    count += 1
                    start = start+1 if i == start+1 else start
                    break
        time += 1
    return time
print(sol())
