import sys; input = sys.stdin.readline

N, M = map(int, input().split())
encyclopedia_list = []
encyclopedia_dict = {}
for i in (range(N)):
    name = input().rstrip()
    encyclopedia_list.append(name)
    encyclopedia_dict[name] = i+1

result = []
for _ in range(M):
    ans = input().rstrip()
    result.append(
        encyclopedia_list[int(ans)-1] 
        if ans.isdigit() 
        else encyclopedia_dict[ans]
    )

print(*result, sep="\n")