import collections
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = re.sub(r'[^\w]', " ", paragraph.lower())
        dic = collections.Counter(s.split())
        for ban in banned: 
            try: dic.pop(ban)
            except: pass
        return dic.most_common(1)[0][0]

S = Solution()
result = S.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
print(result)