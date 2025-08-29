from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, max_ones = -1, 0
        for right in range(len(nums)):
            if nums[right] == 1:
                max_ones = max(right - left, max_ones)
            else:
                left = right
        return max_ones
