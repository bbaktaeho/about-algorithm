from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]):
        digit_logs = []
        char_logs = []
        for log in logs:
            if log.split()[1].isdigit(): digit_logs.append(log)
            else: char_logs.append(log)

        char_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        return char_logs + digit_logs


result = Solution().reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])
print(result)