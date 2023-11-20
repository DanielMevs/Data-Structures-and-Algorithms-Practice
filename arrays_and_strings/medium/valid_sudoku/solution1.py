from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        columns = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # key = (r / 3, c / 3) rounded down

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue

                if (board[row][col] in rows[row] or
                    board[row][col] in columns[col] or
                    board[row][col] in squares[(row // 3, col // 3)]):

                    return False
                
                columns[col].add(board[row][col])
                rows[row].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])
                
        return True
                


