from typing import List


class Solution:
    # Time complexity: O(m * n), space complexity: O(n)
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        dp = [float("inf")] * (COLS + 1)
        dp[COLS - 1] = 0

        for r in reversed(range(ROWS)):
            for c in reversed(range(COLS)):
                dp[c] = grid[r][c] + min(dp[c], dp[c + 1])

        return dp[0]
