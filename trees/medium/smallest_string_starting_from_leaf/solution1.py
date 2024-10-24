from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        def helper(root, curr):
            if not root:
                return

            curr = chr(ord('a') + root.val) + curr
            if root.left and root.right:
                return min(
                    helper(root.left, curr),
                    helper(root.right, curr)
                )

            if root.right:
                return helper(root.right, curr)
            if root.left:
                return helper(root.left, curr)
            return curr

        return helper(root, '')
