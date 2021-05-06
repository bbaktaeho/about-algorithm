import re
class Solution:
    def isPalindrome(self, s: str):
        s = re.sub(r'[^a-z0-9]', "", s.lower())
        return s == s[::-1]

result = Solution().isPalindrome("A man, a plan, a canal: Panama")
print(result)