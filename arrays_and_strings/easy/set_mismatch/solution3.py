from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        x = 0  # duplicate - missing
        y = 0  # duplicate^2 - missing^2

        for i in range(1, N + 1):
            x += nums[i - 1] - i
            y += nums[i - 1]**2 - i**2

        missing = (y - x**2) // (2 * x)
        duplicate = missing + x
        return [duplicate, missing]
