# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: TreeNode) -> str:
        result = []

        def preOrder(root):
            if not root:
                return 
        
            result.append("(")
            result.append(str(root.val))

            if not root.left and root.right:
                result.append("()")

            preOrder(root.left)
            preOrder(root.right)

            result.append(")")

        preOrder(root)
        return ''.join(result)[1:-1]