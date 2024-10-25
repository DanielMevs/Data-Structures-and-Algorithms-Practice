from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(
            self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        stack = [root]
        visit = set()
        parents = {root: None}

        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                if node.val == target:
                    parent = parents[node]
                    if not parent:
                        return None
                    if parent.left == node:
                        parent.left = None
                    if parent.right == node:
                        parent.right = None

            elif node not in visit:
                visit.add(node)
                stack.append(node)
                if node.left:
                    stack.append(node.left)
                    parents[node.left] = node
                if node.right:
                    stack.append(node.right)
                    parents[node.right] = node

        return root
