from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        result = [0] * len(T)
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result

Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])