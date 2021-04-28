# print(input().count(input()))

docs = input()
search = input()

i = 0
count = 0
docs_len = len(docs)
search_len = len(search)

while i + search_len <= docs_len:
    if docs[i : i+search_len] == search: 
        count += 1
        i += search_len
    else: i += 1

print(count)