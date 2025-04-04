from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increase_count = increase_max = 1
        decrease_count = decrease_max = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increase_count += 1
                increase_max = max(
                    increase_max,
                    increase_count)
                decrease_count = 1
            elif nums[i] == nums[i - 1]:
                increase_count = 1
                decrease_count = 1
            else:
                decrease_count += 1
                decrease_max = max(
                    decrease_max,
                    decrease_count)
                increase_count = 1

        return max(decrease_max, increase_max)
