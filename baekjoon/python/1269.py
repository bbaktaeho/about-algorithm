a_len, b_len = map(int, input().split())
A = set(input().split())
B = set(input().split())

ab = A - B
ba = B - A
print(len(ab) + len(ba))