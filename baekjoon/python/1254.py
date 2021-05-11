S = input()
S_len = len(S)
result = S_len * 2 - 1

for i in range(S_len-2, 0, -1):
    S[i]