from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # total = 0
        # nums.sort()
        # for i in range(0, len(nums), 2): total += nums[i]
        # return total
        return sum(sorted(nums)[::2])

print(Solution().arrayPairSum([6,2,6,5,1,2]))