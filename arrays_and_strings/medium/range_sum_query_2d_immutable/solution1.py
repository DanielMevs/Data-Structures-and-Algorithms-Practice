class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        rows, cols = len(matrix), len(matrix[0])
        # - Initializing the sum matrix to be of size +1
        # - the the original to eliminate the edge
        # - case of starting at the first column/row and
        # - going out of bounds.
        self.sumMat = [[0] * (cols + 1) for row in range(rows + 1)]

        # - Calculate/initialize prefix sum for entire matrix
        for row in range(rows):
            prefix = 0
            for col in range(cols):
                prefix += matrix[row][col]
                # print(prefix)
                above = self.sumMat[row][col + 1]
                # print(above)
                self.sumMat[row + 1][col + 1] = prefix + above
                # print(self.sumMat)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # - To offset the 0's padded above and to the left
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.sumMat[row2][col2]
        print(bottomRight)
        above = self.sumMat[row1 - 1][col2]
        print(above)
        left = self.sumMat[row2][col1 - 1]
        print(left)
        topLeft = self.sumMat[row1 - 1][col1 - 1]
        print(topLeft)
        print('-'*20)

        return bottomRight - above - left + topLeft
        

print(NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]).sumRegion(2,1,4,3))