import sys; input =sys.stdin.readline
N = int(input())

postfix = input().rstrip()
postfix_dict = {} # 알파벳을 키 값으로 두고 숫자를 데이터로 초기화

for i in range(N):
    num = int(input())
    postfix_dict[chr(65 + i)] = num

calc = [] # 후위표기식을 계산할 스택
for c in postfix:
    if c in postfix_dict: calc.append(int((postfix_dict[c])))
    else:
        if c == "*": calc.append(calc.pop() * calc.pop())
        if c == "/": 
            back = calc.pop()
            calc.append(calc.pop() / back)
        if c == "+": calc.append(calc.pop() + calc.pop())
        if c == "-": 
            back = calc.pop()
            calc.append(calc.pop() - back)

print("%.2f" % calc[0])