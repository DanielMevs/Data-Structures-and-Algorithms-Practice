from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        count = result = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += nums[i]
            else:
                count = nums[i]

            result = max(count, result)

        return result
