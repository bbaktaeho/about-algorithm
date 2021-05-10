x, y = input().split()
x_len = len(x)
sub_len = len(y) - len(x)

diff = x_len
for i in range(sub_len+1):
    temp_diff = 0
    for j in range(x_len):
        if x[j] != y[i+j]: temp_diff += 1
    diff = min(diff, temp_diff)
print(diff)