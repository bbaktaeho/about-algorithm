N = int(input()) # 학생 수
l = [] # 모든 학생 리스트
for i in range(1, N+1):
    student = list(map(int, input().split()))
    student.append(i) # 학생의 번호를 삽입
    l.append(student)

l.sort(reverse=True)
max_score = l[0][0]
l = list(filter(lambda x: x[0] == max_score, l))
l.sort(key=lambda x: x[1])
min_repeat = l[0][1]
l = list(filter(lambda x: x[1] == min_repeat, l))
l.sort(key=lambda x: x[2])
print(l[0][3])














# # 2. 점수가 같은 학생이 있는지 확인
# # 2.1 점수가 같은 학생이 없다면 0번 인덱스의 학생 번호를 출력
# max_score = l[0][0]
# same_score_list = [l[0]]
# for i in range(1, N):
#     if max_score > l[i][0]: break
#     same_score_list.append(l[i])

# # 3. 제출 횟수를 기준으로 학생을 정렬
# same_score_list.sort(key=lambda x: x[1])

# min_repeat = same_score_list[0][1]
# same_repeat_list = [same_score_list[0]]
# for i in range(1, len(same_score_list)):
#     if min_repeat > same_score_list[i][1]: break
#     same_repeat_list.append(same_score_list[i])

# same_repeat_list.sort(key=lambda x: x[2])
# print(same_repeat_list[0][3])