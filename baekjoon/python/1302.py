# import sys
# input = sys.stdin.readline

# book_list = dict()

# for _ in range(int(input())):
#     book = input().strip()
#     try: book_list[book] += 1
#     except: book_list[book] = 1

# max_sell_count = max(book_list.values())
# best_books = []
# for book, count in book_list.items():
#     if max_sell_count == count: best_books.append(book)
# print(sorted(best_books)[0])

import sys; input = sys.stdin.readline

books = dict()
for _ in range(int(input())):
    book = input().rstrip()
    try: books[book] += 1 
    except: books[book] = 1

best_count = max(books.values())
result = list(filter(lambda x: x[1] == best_count, books.items()))
result.sort()
print(result[0][0])