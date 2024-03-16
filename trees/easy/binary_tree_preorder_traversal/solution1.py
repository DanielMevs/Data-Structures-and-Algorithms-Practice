# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        current, stack = root, []
        result = []
        while current or stack:
            if current:
                result.append(current.val)
                stack.append(current.right)
                current = current.left
            else:
                current = stack.pop()

        return result
        