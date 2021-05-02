while True:
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z == 0: break
    arr = sorted([x, y, z])
    if arr[0]**2 + arr[1]**2 == arr[2]**2:
        print('right')
    else:
        print("wrong")