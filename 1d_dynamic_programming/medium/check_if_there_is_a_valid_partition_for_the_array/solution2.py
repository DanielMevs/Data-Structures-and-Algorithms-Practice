from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = {}

        def dfs(i):
            if i == len(nums):
                return True
            if i in dp:
                return dp[i]

            result = False
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                result = dfs(i + 2)
            if i < len(nums) - 2:
                if (nums[i] == nums[i + 1]
                    == nums[i + 2] or
                        nums[i] + 1 == nums[i + 1] == nums[i + 2] - 1):
                    result = result or dfs(i + 3)

            dp[i] = result
            return result

        return dfs(0)
