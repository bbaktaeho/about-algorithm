class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        for i in range(s_len, 0, -1):
            start, end = 0, i
            while end <= s_len:
                test = s[start:end]
                if test == test[::-1]: return test
                start += 1
                end += 1
        return s[0]

s = Solution()
print(s.longestPalindrome("a"))