from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        current_product = 1
        result = 0
        left, right = 0, 0

        while right < len(nums):
            current_product *= nums[right]
            while current_product >= k and left <= right:
                current_product //= nums[left]
                left += 1

            result += right - left + 1
            right += 1
        
        return result
    