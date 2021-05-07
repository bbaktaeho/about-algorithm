N = input()
n = sorted(N, reverse=True)

def sol(n):
    num = int("".join(n))
    if num % 30 == 0: return num
    else: return -1

print(sol(n))