bracket = input()
stack = []
result = 0

dic = {
    "(": ")",
    "[": "]"
}

# 올바른 괄호열인지 판단
for b in bracket:
    if b in ("(", "["): stack.append(b)
    else:
        if not stack or (dic[stack.pop()] != b): 
            print(0); exit(0)

stack = []
for b in bracket:
    print(stack)
    if stack and not stack[-1].isdigit():
        stack.append("2" if stack.pop() + b == "()" else "3")
    stack.append(b)
print(stack)