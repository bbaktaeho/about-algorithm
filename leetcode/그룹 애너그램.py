from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = collections.defaultdict(list)
        for str in strs: word_dict["".join(sorted(str))].append(str)
        anagrams = word_dict.values()
        return [sorted(result) for result in anagrams]

s = Solution()
result = s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(result)