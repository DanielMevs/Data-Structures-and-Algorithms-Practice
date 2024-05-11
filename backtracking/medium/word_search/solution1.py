class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(row, col, i):
            if i == len(word):
                return True
            if (row < 0 or col < 0 or
               row >= ROWS or col >= COLS or
               word[i] != board[row][col] or
               (row, col) in path):
                return False
            
            path.add((row, col))
            result = (dfs(row + 1, col, i + 1)) or \
                dfs(row - 1, col, i + 1) or \
                dfs(row, col + 1, i + 1) or \
                dfs(row, col - 1, i + 1)
            
            path.remove((row, col))
            return result
        
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
                
        return False
    
