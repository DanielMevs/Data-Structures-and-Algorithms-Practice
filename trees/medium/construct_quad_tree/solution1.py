# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, 
                 topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        def dfs(n, row, col):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[row][col] != grid[row + i][col + j]:
                        allSame = False
                        break
            if allSame:
                return Node(grid[row][col], True)
            
            n = n // 2
            topLeft = dfs(n, row, col)
            topRight = dfs(n, row, col + n)
            bottomLeft = dfs(n, row + n, col)
            bottomRight = dfs(n, row + n, col + n)
            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return dfs(len(grid), 0, 0)