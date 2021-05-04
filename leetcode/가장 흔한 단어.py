import collections
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
       r = re.sub(r'[^\w]', ' ', paragraph).lower().split()
       words = [word for word in r if word not in banned]
       return collections.Counter(words).most_common(1)[0][0]

S = Solution()
a = S.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
print(a)