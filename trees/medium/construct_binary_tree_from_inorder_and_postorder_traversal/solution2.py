# Runtime: O(n)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        inorderIdx = {v: i for i, v in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return None
            
            root = TreeNode(postorder.pop())

            # - Instead of scanning the entiire array
            # we can perform a O(1) operation
            idx = inorderIdx[root.val]
            root.right = helper(idx + 1, right)
            root.left = helper(left, idx - 1)
            return root

        return helper(0, len(inorder) - 1)
