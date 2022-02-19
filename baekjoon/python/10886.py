import sys
input = sys.stdin.readline

N = int(input())
total = 0
for _ in range(N):
    total += int(input())

print("Junhee is cute!" if total > N // 2 else "Junhee is not cute!")
