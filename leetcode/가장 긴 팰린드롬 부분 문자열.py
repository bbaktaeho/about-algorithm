class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     s_len = len(s)
    #     start, end = 0, s_len
    #     while True:
    #         part_str = s[start:end]
    #         if part_str == part_str[::-1]: return part_str
    #         if end >= len(s): 
    #             start = 0 
    #             s_len -= 1
    #             end = s_len
    #         else: start, end = start+1, end+1

    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if len(s) < 2 or s == s[::-1]: return s

        result = ''
        for i in range(len(s) - 1): result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        return result

s = Solution()
print(s.longestPalindrome("123454320"))
