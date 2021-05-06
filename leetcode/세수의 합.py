# 틀림

from itertools import combinations
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_set = set()
        result = [list(comb) for comb in combinations(nums, 3) if sum(comb) == 0]
        for re in result: result_set.add(tuple(sorted(re)))
        return [list(re) for re in result_set]
            
print(Solution().threeSum([0]))