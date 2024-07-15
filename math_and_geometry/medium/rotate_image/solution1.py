from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1
        while left < right:
            for i in range(right-left):
                top, bottom = left, right

                # - Save the topLeft value
                topLeft = matrix[top][left + i]

                # - Move bottom left into top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # - Move bottom right into bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # - Move top right into bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # - Move top left into top right
                matrix[top + i][right] = topLeft

            right -= 1
            left += 1
