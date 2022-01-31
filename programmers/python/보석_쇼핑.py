from collections import defaultdict


def solution(gems):
    gems_length, gems_count = len(gems), len(set(gems))
    gems_dict = defaultdict(lambda: 0)
    start, end = 0, 0
    result_list = []

    while True:
        count = len(gems_dict)
        if start == gems_length:
            break
        if count == gems_count:
            result_list.append((start, end))
            gems_dict[gems[start]] -= 1
            if gems_dict[gems[start]] == 0:
                del gems_dict[gems[start]]
            start += 1
            continue
        if end == gems_length:
            break
        if count != gems_count:
            gems_dict[gems[end]] += 1
            end += 1

    result_list.sort(key=lambda x: x[1]-x[0])
    return [result_list[0][0]+1, result_list[0][1]]
