# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        currentSum = 0

        def dfs(node):
            if not node:
                return
            
            nonlocal currentSum
            dfs(node.right)
            temp = node.val
            node.val += currentSum
            currentSum += temp
            dfs(node.left)
            
        dfs(root)
        return root