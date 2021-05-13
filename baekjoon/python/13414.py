import sys; input = sys.stdin.readline

K, L = map(int, input().split())

waiting = {}
for i in range(L): 
    student = input().rstrip()
    if student in waiting:
        waiting.pop(student)
        waiting[student] = i
    else: waiting[student] = i

result = sorted(list(waiting.items()), key=lambda x: x[1])
for student in result[:K]: print(student[0])