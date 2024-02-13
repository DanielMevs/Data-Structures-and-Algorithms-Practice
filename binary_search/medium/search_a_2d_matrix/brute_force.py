# - O(m * n) runtime

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            for column in row:
                if column == target:
                    return True
        return False