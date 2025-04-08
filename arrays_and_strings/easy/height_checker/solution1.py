from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected_heights = sorted(heights)
        count = 0

        for i, h in enumerate(expected_heights):
            if h != heights[i]:
                count += 1

        return count
