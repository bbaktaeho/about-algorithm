import sys; input = sys.stdin.readline

case = 1

while 1:
    stack = []
    calc_count = 0
    bracket = input().rstrip()
    if bracket[0] == "-": break

    for b in bracket:
        if stack and stack[-1] + b == "{}": stack.pop()
        else: stack.append(b)

    while stack:
        calc_count += 2 if "".join(stack[:2]) == "}{" else 1
        stack = stack[2:]

    print(str(case) + ".", calc_count)
    case += 1