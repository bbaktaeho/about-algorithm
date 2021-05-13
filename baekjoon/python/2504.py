from collections import deque

bracket_dict = {
    "]": ("[", 3),
    ")": ("(", 2)
}

stack = []
data = input();
calc_list = []
result = []
check = 0 # 연속 닫힘 체크
for bracket in data:
    if bracket in ('(', '['): 
        stack.append(bracket)
        check = 0
    else:
        check += 1
        if not stack: 
            result = []
            break
        b_pop = stack.pop()
        couple = bracket_dict[bracket]
        if couple[0] == b_pop: 
            if check >= 2:
                if not stack: 
                    result.append(sum(calc_list) * couple[1])
                    calc_list = []
                else: calc_list.append(calc_list.pop() * couple[1])
            else: 
                calc_list.append(couple[1])
                if not stack: result.append(calc_list.pop())
        else:
            result = []
            break

print(sum(result) if result and not stack else 0)

# 40프로에서 틀림