n, m = map(int, input().split())
card_list = sorted(list(map(int, input().split())))

for _ in range(m):
    total = card_list[0] + card_list[1]
    card_list[0], card_list[1] = total, total
    card_list.sort()

print(sum(card_list))