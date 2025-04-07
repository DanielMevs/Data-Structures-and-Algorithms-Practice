from collections import defaultdict
from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = defaultdict(int)
        result = [0, 0]

        for i in range(n):
            for j in range(n):
                count[grid[i][j]] += 1

        for i in range(1, n ** 2 + 1):
            if i not in count:
                result[1] = i
            if count[i] > 1:
                result[0] = i

        return result
