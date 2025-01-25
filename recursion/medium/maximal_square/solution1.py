from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        max_side_length = 0

        for r in range(1, ROWS + 1):
            for c in range(1, COLS + 1):
                if matrix[r - 1][c - 1] == "1":
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                    max_side_length = max(max_side_length, dp[r][c])

        return max_side_length ** 2
