from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cache = {}

        def dfs(i):
            if i == len(nums):
                return []
            if i in cache:
                return cache[i]

            result = [nums[i]]
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    temp = [nums[i]] + dfs(j)  # O(32)
                    if len(temp) > len(result):
                        result = temp
            cache[i] = result
            return result

        result = []
        for i in range(len(nums)):
            temp = dfs(i)
            if len(temp) > len(result):
                result = temp
        return result
