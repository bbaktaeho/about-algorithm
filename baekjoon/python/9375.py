import sys; input = sys.stdin.readline
import collections

for _ in range(int(input())):
    cloth_dic = collections.defaultdict(int)

    count = int(input())
    for _ in range(count):
        item, key = input().split()
        cloth_dic[key] += 1
    
    result = 1
    for c in cloth_dic.values(): result *= c + 1
    result -= 1
    print(result)
