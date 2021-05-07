import sys; input = sys.stdin.readline
from collections import defaultdict

N = int(input())
for _ in range(N):
    word = list(input().rstrip())
    stack = []
    char_dic = defaultdict(int)
    for char in word:
        if stack and char in char_dic and stack[-1] != char: 
            N -= 1
            break
        stack.append(char)
        char_dic[char] += 1
print(N)