s = input()
s_arr = []
for i in range(len(s)): s_arr.append(s[i:])

for s in sorted(s_arr): print(s)