from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)
        nums = sorted(set(nums))
        result = length
        right = 0

        for left in range(len(nums)):
            while right < len(nums) and nums[right] < nums[left] + length:
                right += 1
            window = right - left
            result = min(result, length - window)
        
        return result

