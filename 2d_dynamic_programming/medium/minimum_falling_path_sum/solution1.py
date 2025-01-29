from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        cache = {}

        def dfs(r, c):
            if r == N:
                return 0
            if c < 0 or c == N:
                return float('inf')
            if (r, c) in cache:
                return cache[(r, c)]

            result = matrix[r][c] + min(
                dfs(r + 1, c - 1),
                dfs(r + 1, c),
                dfs(r + 1, c + 1)
            )

            cache[(r, c)] = result
            return result

        result = float('inf')
        for c in range(N):
            result = min(result, dfs(0, c))

        return result
