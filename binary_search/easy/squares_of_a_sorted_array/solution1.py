from collections import deque


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        output = deque()
        left, right = 0, len(nums) - 1

        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                output.appendleft(nums[left]**2)
                left += 1
            else:
                output.appendleft(nums[right]**2)
                right -= 1
        
        return output