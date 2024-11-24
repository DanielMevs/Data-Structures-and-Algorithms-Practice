from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque([(0, 0, 1)])  # row, col, length
        visited = set((0, 0))
        directions = [
            (-1, -1), (-1, 0),
            (-1, 1), (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        while queue:
            row, col, length = queue.popleft()
            if (min(row, col) < 0 or max(row, col) >= n or
                    grid[row][col]):
                continue
            if row == n - 1 and col == n - 1:
                return length
            for dr, dc in directions:
                if (row + dr, col + dc) not in visited:
                    queue.append((row + dr, col + dc, length + 1))
                    visited.add((row + dr, col + dc))

        return -1
