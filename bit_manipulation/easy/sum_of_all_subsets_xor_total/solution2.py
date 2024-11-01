# O(n) runtime.
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result = result | n

        return result * 2**(len(nums) - 1)
