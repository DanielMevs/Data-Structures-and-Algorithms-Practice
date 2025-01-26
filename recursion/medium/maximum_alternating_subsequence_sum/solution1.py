from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}

        # i = index, even = truse/false
        def dfs(i, even):
            if i == len(nums):
                return 0
            if (i, even) in dp:
                return dp[(i, even)]

            total = nums[i] if even else -nums[i]
            dp[(i, even)] = max(total + dfs(i + 1, not even), dfs(i + 1, even))
            return dp[(i, even)]

        return dfs(0, True)
