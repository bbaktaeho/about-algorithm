def solution(lottos, win_nums):
    zero_count = lottos.count(0) # 0의 개수
    result = 0 # 맞은 번호 개수
    for i in range(6):
        if lottos[i] == 0: continue
        if lottos[i] in win_nums: result += 1
    
    best = result + zero_count
    worst = result
    return [7 - (best if best else 1), 7 - (worst if worst else 1)]