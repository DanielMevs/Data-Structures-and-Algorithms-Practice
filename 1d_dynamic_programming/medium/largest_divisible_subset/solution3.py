from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[num] for num in nums]
        result = []

        for i in reversed(range(len(nums))):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    temp = [nums[i]] + dp[j]
                    dp[i] = temp if len(temp) > len(dp[i]) else dp[i]
            result = dp[i] if len(dp[i]) > len(result) else result
        return result
