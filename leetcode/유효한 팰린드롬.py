# 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 함
import re
s = input().lower()
s = re.sub(r"[^a-z0-9]", "", s)
print(s == s[::-1])