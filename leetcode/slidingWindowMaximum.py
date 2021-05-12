from typing import Deque, List
from collections import deque

# 첫 윈도우에서 최대값을 찾아서 큐의 맨 앞으로 올 수 있도록 한다.
# [1, 3, -1]  -> [3, -1]
# [1, 3, -1] -3  -> []
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0: return []
        if k == 1: return nums
        
        # q = deque()
        
        # def clear(i):
        #     # 1번째 원소 날리기
        #     if q and q[0] == i - k: q.popleft()
        #     while q and nums[q[-1]] < nums[i]: q.pop()

        # for i in range(k):
        #     clear(i)
        #     q.append(i)

        # result = [nums[q[0]]]

        # for i in range(k, n):
        #     clear(i)
        #     q.append(i)
        #     result.append(nums[q[0]])

        # return result

ans = Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
ans = Solution().maxSlidingWindow([7,2,4], 2)
print(ans)