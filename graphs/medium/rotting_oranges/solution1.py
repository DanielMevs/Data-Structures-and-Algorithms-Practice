# - O(n x m) time and space complexity
from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        oranges = deque()
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0]) 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    oranges.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and oranges:
            for i in range(len(oranges)):
                r, c = oranges.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # if in bounds and nonrotten, make rotten
                    # and add to q
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        oranges.append((row, col))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1