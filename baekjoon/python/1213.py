import collections

name = input()
name_len = len(name)
name_set_len = len(set(name))
counter_dict = collections.Counter(name)
l = counter_dict.most_common(name_set_len)

result = ""

if name_len % 2 == 0 and name_len // 2 == name_set_len: 
    for c in sorted(l, key=lambda x: x[0][0]): result += c[0][0]
    print(result + result[::-1])
elif name_len % 2 == 1 and name_len // 2 + 1 == name_set_len and l[0][1] <= 2: 
    for c in sorted(l, key=lambda x: x[0][0]): result += c[0][0]
    print(result + result[::-1][1:])
else: print("I'm Sorry Hansoo")

