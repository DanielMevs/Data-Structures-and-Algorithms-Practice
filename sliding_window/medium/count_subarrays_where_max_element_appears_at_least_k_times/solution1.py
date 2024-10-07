from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count, result = 0, 0
        left, right = 0, 0
        maxNum = max(nums)
        
        while right < len(nums):
            if nums[right] == maxNum:
                count += 1
            while count == k:
                if nums[left] == maxNum:
                    count -= 1
                left += 1
            result += left
            right += 1
        
        return result
    