from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # - Count number of subarrays where current_sum <= x
        def helper(x):
            if x < 0:
                return 0
            
            result = 0
            left, current_sum = 0, 0
            for right in range(len(nums)):
                current_sum += nums[right]
                while current_sum > x:
                    current_sum -= nums[left]
                    left += 1
                
                result += right - left + 1
            
            return result

        return helper(goal) - helper(goal - 1)
    