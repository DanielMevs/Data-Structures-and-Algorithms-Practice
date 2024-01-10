class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        left, right = 0, k - 1
        result = float("inf")
        

        while right < len(nums):
            result = min(result, abs(nums[left] - nums[right]))
            left, right = left + 1, right + 1
        
        return result