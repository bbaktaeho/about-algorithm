s = input()

def rot13(c):
    code = ord(c)
    if 65 <= code <= 90: return code + 13 if code + 13 <= 90 else (code + 13) - 91 + 65
    elif 97 <= code <= 122: return code + 13 if code + 13 <= 122 else (code + 13) - 123 + 97

result = ""
for c in s:
    if c.isalpha(): result += (chr(rot13(c)))
    else: result += c

print(result)