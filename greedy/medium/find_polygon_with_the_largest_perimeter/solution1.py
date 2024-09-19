from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        result = -1
        total = 0

        for n in nums:
            if total > n:
                result = total + n
            total += n

        return result