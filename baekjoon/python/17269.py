n, m = map(int, input().split())
name1, name2 = input().split()

alpha = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
minLength = min(n, m)
total = ""
for i in range(minLength):
    total += name1[i] + name2[i]
total += name1[minLength:] + name2[minLength:]
result = list(map(lambda x: alpha[ord(x) - 65], total))
while len(result) > 2:
    arr = []
    for i in range(0, len(result) - 1):
        plus = result[i] + result[i + 1]
        arr.append(plus % 10 if plus >= 10 else plus)
    result = arr

print("{}%".format(int(str(result[0]) + str(result[1]))))
# 28776kb,68ms

n, m = map(int, input().split())
name1, name2 = input().split()

alpha = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
minLength = min(n, m)
total = ""
for i in range(minLength):
    total += name1[i] + name2[i]
total += name1[minLength:] + name2[minLength:]
result = [alpha[ord(i) - ord("A")] for i in total]

for i in range(len(result) - 2):
    for j in range(len(result) - 1 - i):
        result[j] += result[j + 1]

print("{}%".format(result[0] % 10 * 10 + result[1] % 10))

# 1. 두 이름 중 짧은 길이 찾기
# 2. 번갈아가며 이름 적기
arr = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
char_A = ord('A')
A_len, B_len = map(int, input().split())
min_len = min(A_len, B_len)
A, B = input().split()
total_name = ""
for i in range(min_len): total_name += A[i] + B[i]
total_name += A[min_len:] + B[min_len:]
total = [ arr[ord(c)-char_A] for c in total_name ]
while len(total) > 2:
    temp = []
    for i in range(len(total)-1): temp.append((total[i]+total[i+1]) % 10)
    total = temp
print(str(int("".join(map(str, total))))+"%")