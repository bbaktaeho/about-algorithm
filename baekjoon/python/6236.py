import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
days = []
for _ in range(N):
    days.append(int(readline()))

answer, left, right = sum(days), 0, sum(days)

while left <= right:
    mid = (left + right) // 2
    count, money = 0, 0
    lack = False

    for d in days:
        if mid - d < 0:
            # 돈을 뽑아도 하루를 못 넘기면
            lack = True
            break
        elif money - d < 0:
            money = mid
            count += 1
        money -= d

    # 돈이 부족한 날이 없으면
    if not lack:
        # 목표 횟수보다 count가 같거나 작으면 돈을 줄임
        if count <= M:
            right = mid - 1
            if mid < answer:
                answer = mid
        # 목표 횟수보다 count가 크면 돈을 늘림
        elif count > M:
            left = mid + 1
    # 돈이 부족한 날이 있으면 무조건 돈을 늘림
    else:
        left = mid+1

print(answer)