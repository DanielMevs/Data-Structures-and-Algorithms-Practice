from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        current_sum = count = 0
        n = len(nums) - 1

        for i in range(n):
            current_sum += nums[i]
            remain = total - current_sum
            if current_sum >= remain:
                count += 1

        return count
