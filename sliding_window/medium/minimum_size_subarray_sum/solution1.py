class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        total = 0
        left = 0
        result = float('inf')
        

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                result = min(right - left + 1, result)
                total -= nums[left]
                left += 1

            
        return 0 if result == float('inf') else result
            
            
            
        