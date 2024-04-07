# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:
        def generate(left, right):
            dp = {}
            if left > right:
                return [None]
            
            if (left, right) in dp:
                return dp[(left, right)]
            
            result = []
            for val in range(left, right + 1):
                root = TreeNode(val)
                for leftTree in generate(left, val - 1):
                    for rightTree in generate(val + 1, right):
                        root = TreeNode(val, leftTree, rightTree)
                        result.append(root)
            dp[(left, right)] = result

            return result
        
        return generate(1, n)