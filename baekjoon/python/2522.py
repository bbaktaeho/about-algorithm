n = int(input())
for i in range(-n+1, n):
    print(" "*abs(i) + "*"*(n - abs(i)))