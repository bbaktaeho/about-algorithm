from typing import List


class Solution:
    # def trap(self, height: List[int]) -> int:
    #     if not height: return 0
        
    #     left, right = 0, len(height) - 1
    #     left_max, right_max = height[left], height[right]

    #     volume = 0
    #     while left < right:
    #         left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

    #         if left_max <= right_max:
    #             volume += left_max - height[left]
    #             left += 1
    #         else:
    #             volume += right_max - height[right]
    #             right -= 1
    #     return volume

    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack): break

                distance = i - stack[-1] - 1
                water = min(height[stack[-1]], height[i]) - height[top]
                volume += distance * water
            stack.append(i)
        return volume

print(Solution().trap_3([0,1,0,2,1,0,1,3,2,1,2,1]))