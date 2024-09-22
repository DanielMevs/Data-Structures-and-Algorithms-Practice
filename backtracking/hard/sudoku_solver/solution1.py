from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_possible(row: int, col: int, num: str) -> bool:
            # - Check if the number is already in the row or column
            for i in range(9):
                # - board[row][i] is the i-th column in the row
                # - board[i][col] is the i-th row in the column
                if board[row][i] == num or board[i][col] == num:
                    return False

            # - Check if the number is already in the 3x3 box
            # - Start row and start column constitute the top-left corner
            #  of the 3x3 box in consideration
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)

            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False

            return True
        
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for num in '123456789':
                        if is_possible(row, col, num):
                            board[row][col] = num
                            if self.solveSudoku(board):
                                return True
                            board[row][col] = '.'

                    return False
            
        return True