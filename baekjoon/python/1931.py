import sys; input = sys.stdin.readline

N = int(input())
conf_list = []
for _ in range(N):
    conf = tuple(map(int, input().split()))
    conf_list.append(conf)

conf_list.sort(key=lambda x: (x[1], x[0]))
cur_conf = conf_list[0]
count = 1
for i in range(1, N):
    if cur_conf[1] <= conf_list[i][0]:
        cur_conf = conf_list[i]
        count += 1

print(count)
