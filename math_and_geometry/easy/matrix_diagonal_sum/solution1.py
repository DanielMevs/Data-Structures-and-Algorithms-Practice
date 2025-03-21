from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        row, col = len(mat), len(mat[0])
        for i in range(row):
            result += mat[i][i] + mat[i][col - i - 1]

        if row % 2:
            result -= mat[row // 2][row // 2]

        return result
