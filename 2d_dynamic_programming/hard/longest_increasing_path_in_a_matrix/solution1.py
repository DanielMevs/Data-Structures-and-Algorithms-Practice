class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}  # (r, c) -> LIP

        def dfs(r, c, prevVal):
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                    matrix[r][c] <= prevVal):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            
            result = 1
            result = max(result, 1 + dfs(r + 1, c, matrix[r][c]))
            result = max(result, 1 + dfs(r - 1, c, matrix[r][c]))
            result = max(result, 1 + dfs(r, c + 1, matrix[r][c]))
            result = max(result, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = result
            return result

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        
        return max(dp.values())