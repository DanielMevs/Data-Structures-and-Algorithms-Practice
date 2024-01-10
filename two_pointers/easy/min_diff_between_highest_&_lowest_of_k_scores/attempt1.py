'''Did not take into account that the window size is k'''

class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        left, right = 0, 1
        result = abs(nums[left] - nums[right]) if len(nums) > 1 else 0
        left, right = left + 1, right + 1

        while right < len(nums):
            result = min(result, abs(nums[left] - nums[right]))
            left, right = left + 1, right + 1
        
        return result
            

        
        
        