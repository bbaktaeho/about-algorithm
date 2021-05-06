from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()
        for i, num in enumerate(nums): num_dict[num] = i
        for i, num in enumerate(nums):
            if target - num in num_dict and i != num_dict[target-num]: return [i, num_dict[target-num]]