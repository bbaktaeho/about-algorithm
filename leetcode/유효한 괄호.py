class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []

        for b in s:
            if b not in bracket: stack.append(b)
            elif not stack or bracket[b] != stack.pop(): return False
        return len(stack) == 0 
    
print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("(]"))
print(Solution().isValid("([)]"))
print(Solution().isValid("{[]}"))