def solution(paths):
    result = [] # 결과 리스트
    step_list = [paths[0][0]] # 직선 단계별 리스트
    next_step = paths[0][1] # 직선의 다음 수
    is_asc = paths[0][0] < paths[0][1] # 증가 또는 감소하는 직선인지 확인

    for i in range(1, len(paths)): # 두 번째 직선부터 시작
        if next_step != paths[i][0]:
            step_list.append(next_step)
            result.append(step_list)
            step_list = [] # 단계 초기화
            step_list.append(paths[i][0])
        next_step = paths[i][1]
    step_list.append(next_step)
    result.append(step_list)

    ans = set()
    print(result)
    for x, y in sorted(result):
        a
        ans.append(x); ans.append(y)
    
    print(ans)




    # asc_list = list(filter(lambda x: x[0] < x[1], sorted(paths)))
    # desc_list = list(filter(lambda x: x[0] > x[1], sorted(paths, reverse=True)))

    # result = [asc_list[0][0]] # 결과

    # asc_num = asc_list[0][1]
    # # 오름차순 직선
    # for i in range(1, len(asc_list)):
    #     if asc_num != asc_list[i][0]: 
    #         result.append(asc_num)
    #         result.append(asc_list[i][0])
    #     asc_num = asc_list[i][1]
    # result.append(asc_list[-1][1]) # 오름차순 직선의 끝 넣기

    # result.append(desc_list[0][0]) # 내림차순 직선의 
    # desc_num = desc_list[0][1]
    # # 내림차순 직선
    # for i in range(1, len(desc_list)):
    #     if desc_num != desc_list[i][0]:
    #         result.append(desc_num)
    #         result.append(desc_list[i][0])
    #     desc_num = desc_list[i][1]
    # result.append(desc_list[-1][1])
    
    # return result


solution([[1,2], [2,3], [3,4], [8,7], [7,6]])
solution([[1,2], [4,5], [10,9], [3,4]])