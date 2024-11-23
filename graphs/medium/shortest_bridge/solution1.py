from typing import List
from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def invalid(row, col):
            return row < 0 or col < 0 or row == n or col == n

        visited = set()

        def dfs(row, col):
            if (
                invalid(row, col) or
                    not grid[row][col] or
                    (row, col) in visited):
                return
            visited.add((row, col))
            for dr, dc in directions:
                dfs(row + dr, col + dc)

        def bfs():
            result, queue = 0, deque(visited)
            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    for dr, dc in directions:
                        currentRow, currentCol = row + dr, col + dc
                        if (
                            invalid(currentRow, currentCol) or
                                (currentRow, currentCol) in visited):
                            continue
                        if grid[currentRow][currentCol]:
                            return result
                        queue.append([currentRow, currentCol])
                        visited.add((currentRow, currentCol))
                result += 1

        for row in range(n):
            for col in range(n):
                if grid[row][col]:
                    dfs(row, col)
                    return bfs()
