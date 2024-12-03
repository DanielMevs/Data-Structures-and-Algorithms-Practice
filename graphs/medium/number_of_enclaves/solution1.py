from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # Return num of land cells
        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                    not grid[r][c] or (r, c) in visited):
                return 0
            visited.add((r, c))
            result = 1
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                result += dfs(r + dr, c + dc)
            return result

        visited = set()
        land, borderLand = 0, 0
        for row in range(ROWS):
            for col in range(COLS):
                land += grid[row][col]
                if (grid[row][col] and (row, col) not in visited and
                        (col in [0, COLS - 1] or row in [0, ROWS - 1])):
                    borderLand += dfs(row, col)

        return land - borderLand
