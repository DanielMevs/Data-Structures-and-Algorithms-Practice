from typing import List


class Solution:
    def countSubIslands(
            self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        visited = set()

        def dfs(row, col):
            if (row < 0 or col < 0 or row == ROWS or
                col == COLS or
                grid2[row][col] == 0 or
                    (row, col) in visited):
                return True

            visited.add((row, col))
            result = True
            if grid1[row][col] == 0:
                result = False

            result = dfs(row - 1, col) and result
            result = dfs(row + 1, col) and result
            result = dfs(row, col - 1) and result
            result = dfs(row, col + 1) and result
            return result

        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if (grid2[row][col] and
                    (row, col) not in visited
                        and dfs(row, col)):
                    count += 1
        return count
