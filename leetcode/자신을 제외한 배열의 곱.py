from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_size = len(nums)
        output = []
        p = 1
        for i in range(nums_size):
            output.append(p)
            p *= nums[i]
        p = 1
        for i in range(nums_size-1, -1, -1):
            output[i] *= p
            p *= nums[i]
        return output

print(Solution().productExceptSelf([1,2,3,4]))