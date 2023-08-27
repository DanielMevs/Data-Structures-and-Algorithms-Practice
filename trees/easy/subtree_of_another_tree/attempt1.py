# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: [TreeNode], subRoot: [TreeNode]) -> bool:
        
        
        
        
        if self.sameTree(root, subRoot):
            isEqual = (
                self.isSubtree(root.left, subRoot.left) and
                self.isSubtree(root.right, subRoot.right)
            )

            return isEqual
            
        
    def sameTree(self, root: [TreeNode], subRoot: [TreeNode]) -> bool:
        return root.val == subRoot.val