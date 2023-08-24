class Solution:
    def maxArea(self, height: list[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1

        while left < right:
            area = (right - 1) * min(height[left], height[right])
            result = max(result, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return result
