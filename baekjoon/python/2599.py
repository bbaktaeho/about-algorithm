import sys; input = sys.stdin.readline

n = int(input())
school = []
check = True
for i in range(0, 3):
    x, y = map(int, input().split())
    school.append(x)
    school.append(y)

for i in range(0, school[0]+1): # 0부터 A남자의 수
    a = i # AB
    d = school[0] - a # AC
    e = school[5] - d # BC
    b = school[2] - e # BA
    c = school[1] - b # CA
    f = school[4] - c # CB
    
    if a >= 0 and b >= 0 and c >= 0 and d >=0 and e >= 0 and f >=0:
        print(1)
        print(a, d)
        print(b, e)
        print(c, f)
        check = False
        break

if check:
    print(0)