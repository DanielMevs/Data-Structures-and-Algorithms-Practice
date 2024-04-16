# O(n) average time;
# O(h) memory where h = height of tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.updateStack(root)

    def next(self) -> int:
        result = self.stack.pop()
        current = result.right
        self.updateStack(current)
        
        return result.val

    def hasNext(self) -> bool:
        return self.stack != [] 

    def updateStack(self, current: TreeNode) -> None:
        while current:
            self.stack.append(current)
            current = current.left
