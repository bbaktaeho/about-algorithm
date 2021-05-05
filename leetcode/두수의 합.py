from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = dict()
        for i, v in enumerate(nums): num_dic[v] = i

        for i, v in enumerate(nums):
            if target - v in num_dic and i != num_dic[target - v]:
                return [i, num_dic[target-v]]
