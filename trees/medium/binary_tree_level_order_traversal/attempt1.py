from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: [TreeNode]) -> [list[int]]:
        if not root:
            return []

        result = []
        
        q = deque([root])

        while q:
            
            result.append([x.val for x in q if x != []])

            node = q.popleft()


            if not node:
                continue
            if not node.left:
                q.append(None)
            else:
                q.append(node.left)
            if not node.right:
                q.append(None)
            else:
                q.append(node.right)

        return result


