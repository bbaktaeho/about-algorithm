x, y = input().split()
sub_len = len(y) - len(x)
if sub_len == 0:
    diff = 0
    for i in range(len(x)):
        if x[i] != y[i]: diff += 1
    print(diff)
else: 
    diff = len(y)
    for i in range(sub_len):
        temp_diff = 0
        for j in range(len(x)):
            if x[j] != y[j+i]: temp_diff += 1 
        diff = min(diff, temp_diff)
    print(diff)