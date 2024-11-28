from typing import List
from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        for row in range(n):
            for col in range(n):
                if grid[row][col]:
                    queue.append([row, col])

        result = -1
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while queue:
            row, col = queue.popleft()
            result = grid[row][col]
            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc
                if (
                    min(newRow, newCol) >= 0 and
                    max(newRow, newCol) < n and
                        grid[newRow][newCol] == 0):
                    queue.append([newRow, newCol])
                    grid[newRow][newCol] = grid[row][col] + 1

        return result - 1 if result > 1 else -1
