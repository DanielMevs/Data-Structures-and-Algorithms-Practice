from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid)
        cache = {}

        def helper(r, c):
            if r == N - 1:
                return grid[r][c]
            if (r, c) in cache:
                return cache[(r, c)]

            result = float('inf')

            for next_col in range(N):
                if next_col != c:
                    result = min(
                        result,
                        grid[r][c] + helper(r + 1, next_col)
                    )
                    cache[(r, c)] = result

            return result

        result = float('inf')
        for c in range(N):
            result = min(result, helper(0, c))

        return result
