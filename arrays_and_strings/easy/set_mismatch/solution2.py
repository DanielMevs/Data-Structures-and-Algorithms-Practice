from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = [0, 0]  # duplicate, missing

        for n in nums:
            n = abs(n)
            if nums[n - 1] < 0:
                result[0] = n
            nums[n - 1] = -nums[n - 1]

        for i, n in enumerate(nums):
            if n > 0 and i + 1 != result[0]:
                result[1] = i + 1
                return result
            