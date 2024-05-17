from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows, columns = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(current_row, current_col):
            queue = deque()
            visited.add((current_row, current_col))
            queue.append((current_row, current_col))

            # - While there are still elements in the queue,
            # i.e. there are adjacent islands to current coordinates
            while queue:
                row, column = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for direction_row, direction_column in directions:
                    rw, col = row + direction_row, column + direction_column

                    is_adjacent = (rw) in range(rows) and \
                        (col) in range(columns) and \
                        grid[rw][col] == '1' and \
                        (rw, col) not in visited

                    if is_adjacent:
                        queue.append((rw, col))
                        visited.add((rw, col))

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1" and (row, column) not in visited:
                    bfs(row, column)
                    islands += 1
        
        return islands
        