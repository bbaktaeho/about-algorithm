# N, M = map(int, input().split())
# team = dict()
# while N != 0:
#     teamName = input()
#     team[teamName] = [input() for _ in range(int(input()))]
#     N -= 1
# while M != 0:
#     quiz, check = input(), int(input())
#     if check:
#         for k, v in team.items():
#             if quiz in v:
#                 print(k)
#                 break
#     else:
#         for i in sorted(team.get(quiz)):
#             print(i)
#     M -= 1

# N, M = map(int, input().split())

# teamMem, memTeam = {}, {}
# for _ in range(N):
#     teamName, memNum = input(), int(input())
#     teamMem[teamName] = []
#     for _ in range(memNum):
#         name = input()
#         teamMem[teamName].append(name)
#         memTeam[name] = teamName

# for i in range(M):
#     quiz, check = input(), int(input())
#     if check:
#         print(memTeam[quiz])
#     else:
#         for mem in sorted(teamMem[quiz]):
#             print(mem)

import sys; input = sys.stdin.readline
N, M = map(int, input().split())

team_list = {}
member_list = {}

for _ in range(N):
    team_n = input().rstrip()
    team_p = int(input())
    team = [input().rstrip() for _ in range(team_p)]
    for member in team: member_list[member] = team_n
    team_list[team_n] = team
    
for _ in range(M):
    quiz = input().rstrip()
    is_member = int(input())
    if is_member: print(member_list[quiz])
    else: print("\n".join(sorted(team_list[quiz])))
