# 모든 알파벳이 짝수일 때 팰린드롬
# 두 개 이상의 알파벳이 홀수일 때 X
import sys; input = sys.stdin.readline
import collections

name = input().rstrip()
name_dic = collections.Counter(name)
name_len = len(name)

odd = 0
for count in name_dic.values():
    if count % 2 != 0: odd += 1

if odd >= 2: print("I'm Sorry Hansoo")
else:
    result = ""
    front = ""
    for c, count in name_dic.items():
        if count % 2 != 0:
            if count == 1:
                result = c * count
                name_dic.pop(c)
                break
            else:
                result = c
                break
    for c in sorted(name_dic): front += c * (name_dic[c] // 2)
    print(front + result + front[::-1])
