n = int(input())
B = list(map(int, input().split()))

A = [B[0]] * n
for i in range(1, len(B)): A[i] = B[i] * (i+1) - sum(A[:i])
print(*A)