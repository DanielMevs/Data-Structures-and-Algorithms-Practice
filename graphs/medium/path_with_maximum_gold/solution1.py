from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, visited):
            if (
                min(r, c) < 0 or r == ROWS or c == COLS or
                grid[r][c] == 0 or (r, c) in visited
            ):
                return 0
            visited.add((r, c))
            result = grid[r][c]
            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for r2, c2 in neighbors:
                result = max(result, grid[r][c] + dfs(r2, c2, visited))
            visited.remove((r, c))
            return result

        result = 0
        for r in range(ROWS):
            for c in range(COLS):
                result = max(result, dfs(r, c, set()))
        return result
