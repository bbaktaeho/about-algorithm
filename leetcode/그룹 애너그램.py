from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for str in strs:
            dic["".join(sorted(str))].append(str)
        return list(dic.values())

s = Solution()
s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])