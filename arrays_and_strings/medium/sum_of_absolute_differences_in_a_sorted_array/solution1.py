from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        left_sum = 0
        result = []

        for i, num in enumerate(nums):
            right_sum = total_sum - num - left_sum
            left_size, right_size = i, len(nums) - i - 1
            result.append(
                left_size * num - left_sum + right_sum - right_size * num
            )
            left_sum += num

        return result