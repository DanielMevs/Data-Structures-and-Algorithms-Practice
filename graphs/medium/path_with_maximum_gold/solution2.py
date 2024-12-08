from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                min(r, c) < 0 or r == ROWS or c == COLS or
                    grid[r][c] == 0
            ):
                return 0

            temp = grid[r][c]
            grid[r][c] = 0  # mark spot as visited
            result = 0
            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

            for r2, c2 in neighbors:
                result = max(result, temp + dfs(r2, c2))

            grid[r][c] = temp  # readd gold to backtrack
            return result

        result = 0
        for r in range(ROWS):
            for c in range(COLS):
                result = max(result, dfs(r, c))

        return result
