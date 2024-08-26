from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = max2 = 0  # largest, second largest
        min1 = min2 = float("inf")  # smallest, second smallest

        for n in nums:
            if n > max2:
                if n > max1:
                    max1, max2 = n, max1
                else:
                    max2 = n
            if n < min2:
                if n < min1:
                    min1, min2 = n, min1
                else:
                    min2 = n

        return (max1 * max2) - (min1 * min2)
