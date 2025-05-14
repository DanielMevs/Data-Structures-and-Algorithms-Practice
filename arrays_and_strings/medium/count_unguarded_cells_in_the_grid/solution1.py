from typing import List


class Solution:
    # 0 = free; 1 = guard; 2 = wall; 3 = guardable
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]],
            walls: List[List[int]]) -> int:

        grid = [[0] * n for _ in range(m)]

        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2

        def mark_guarded(r, c):
            for row in range(r + 1, m):  # look down
                if grid[row][c] in [1, 2]:
                    break
                grid[row][c] = 3
            for row in reversed(range(0, r)):  # look up
                if grid[row][c] in [1, 2]:
                    break
                grid[row][c] = 3
            for col in range(c + 1, n):  # look right
                if grid[r][col] in [1, 2]:
                    break
                grid[r][col] = 3
            for col in reversed(range(0, c)):  # look left
                if grid[r][col] in [1, 2]:
                    break
                grid[r][col] = 3

        for r, c in guards:
            mark_guarded(r, c)
        result = 0
        for row in grid:
            for cell in row:
                if not cell:
                    result += 1

        return result
