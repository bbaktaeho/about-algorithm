def solution(N, sequence):
    start = 1 # 1번 부터 시작
    total = 0 # 최소 시간

    for home in sequence:
        time = abs(home - start)
        total += min(time, N - time)
        start = home
    
    return total


# print(solution(5, [1,2,3,4,5]))
print(solution(5, [3,5,4,1,2]))