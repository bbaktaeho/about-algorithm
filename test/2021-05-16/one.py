def solution(stats):
    team_list = [] # 팀을 담을 리스트

    for stat in stats:
        # 팀이 없을 때
        if not team_list: team_list.append([stat])
        else:
            # 가장 최근에 참여한 플레이어보다 낮을 때
            if team_list[-1][-1] > stat: 
                team_list.append([stat])
            # 가장 최근에 참여한 플레이어보다 높을 때
            else:
                for team in team_list:
                    if team[-1] < stat: 
                        team.append(stat)
                        break
    
    return len(team_list)

print(solution([5, 3, 4, 6, 2, 1]))
print(solution([6, 2, 3, 4, 1, 5]))