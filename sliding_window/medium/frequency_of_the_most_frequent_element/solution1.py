class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()

        left, right = 0, 0
        result, total = 0, 0

        while right < len(nums):
            total += nums[right]

            while nums[right] * (right - left + 1) > k + total:
                total -= nums[left]
                left += 1
            result = max(result, right - left + 1)
            right += 1
        
        return result
