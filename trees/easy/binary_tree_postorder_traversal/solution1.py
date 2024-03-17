# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        stack = [root]
        visits = [False]
        result = []

        while stack:
            current, visited = stack.pop(), visits.pop()
            if current:
                if visited:
                    result.append(current.val)
                else:
                    stack.append(current)
                    visits.append(True)
                    stack.append(current.right)
                    visits.append(False)
                    stack.append(current.left)
                    visits.append(False)
        
        return result
            
