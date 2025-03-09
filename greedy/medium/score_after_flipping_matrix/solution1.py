from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            if grid[r][0] == 0:
                for c in range(COLS):
                    grid[r][c] = 1 - grid[r][c]

        for c in range(COLS):
            one_count = 0
            for r in range(ROWS):
                one_count += grid[r][c]
            if one_count < ROWS - one_count:
                for r in range(ROWS):
                    grid[r][c] = 1 - grid[r][c]

        result = 0
        for r in range(ROWS):
            for c in range(COLS):
                result += grid[r][c] << (COLS - 1 - c)

        return result
