a, b = input().split()

result = int(str(int(a[::-1]) + int(b[::-1]))[::-1])
print(result)
