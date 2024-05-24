class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxArea = 0
        left, right = 0, len(height) - 1
        while left < right:
            bottleNeck = min(height[left], height[right])
            runningArea = bottleNeck * (right - left)
            maxArea = max(maxArea, runningArea)
            if height[right] <= height[left]:
                right -= 1
            else:
                left += 1
        return maxArea
