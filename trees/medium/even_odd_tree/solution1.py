from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        even = True
        queue = deque([root])

        while queue:
            prev = float('-inf') if even else float('inf')
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()

                if even and (node.val % 2 == 0 or node.val <= prev):
                    return False
                elif not even and (node.val % 2 == 1 or node.val >= prev):
                    return False

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                prev = node.val

            even = not even

        return True
