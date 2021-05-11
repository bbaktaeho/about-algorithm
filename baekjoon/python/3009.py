x_arr, y_arr = [], []
for _ in range(3):
    x, y = map(int, input().split())
    if x in x_arr: x_arr.remove(x)
    else: x_arr.append(x)
    if y in y_arr: y_arr.remove(y)
    else: y_arr.append(y)
print(x_arr[0], y_arr[0])