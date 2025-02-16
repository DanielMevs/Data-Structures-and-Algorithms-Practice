from typing import List


class Solution:
    # O(N^3) time, O(N) space
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid)
        prev = grid[0]

        for r in range(1, N):
            dp = [float('inf')] * N
            for current_c in range(N):
                for prev_c in range(N):
                    if prev_c != current_c:
                        dp[current_c] = min(
                            dp[current_c],
                            grid[r][current_c] + prev[prev_c]
                        )
            prev = dp

        return min(prev)
