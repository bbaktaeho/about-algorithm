from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n  = len(height)
        if n == 0: return 0

        lmax = [0] * n
        rmax = [0] * n
        lmax[0] = height[0]
        rmax[n-1] = height[n-1]
        for i in range(1, n):
            lmax[i] = max(lmax[i-1], height[i])
        for i in range(n-2, -1, -1):
            rmax[i] = max(rmax[i+1], height[i])
        
        ans = 0
        # 교집합 구하기
        for i in range(n):
            ans += min(lmax[i], rmax[i]) - height[i]
        return ans

s = Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(s)