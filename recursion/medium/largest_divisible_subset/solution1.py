from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cache = {}  # (i, prev) -> subset

        def dfs(i, prev):
            if i == len(nums):
                return []
            if (i, prev) in cache:
                return cache[(i, prev)]

            result = dfs(i + 1, prev)  # skip nums[i]
            if nums[i] % prev == 0:
                temp = [nums[i]] + dfs(i + 1, nums[i])  # include nums[i]
                result = temp if len(temp) > len(result) else result

            cache[(i, prev)] = result
            return result

        return dfs(0, 1)
