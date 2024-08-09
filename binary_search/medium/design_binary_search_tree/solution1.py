from typing import List


class TreeNode:
    def __init__(self, key=None, val=None, right=None, left=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:      
        newNode = TreeNode(key, val)
        if not self.root:
            self.root = newNode
            return
        
        curr = self.root
        while True:
            # Go left
            if key < curr.key:
                if not curr.left:
                    curr.left = newNode
                    return
                curr = curr.left

            # Go right                
            elif key > curr.key:
                if not curr.right:
                    curr.right = newNode
                    return
                curr = curr.right                
            else:
                # Override val at key
                curr.val = val
                return
        
    def get(self, key: int) -> int:
        if not self.root:
            return -1
        
        curr = self.root
        while curr:
            # Go left
            if key < curr.key:
                curr = curr.left

            # Go right                
            elif key > curr.key:
                curr = curr.right                
            else:
                # return val at key
                return curr.val
        return -1

    def getMin(self) -> int:
        curr = self.findMin(self.root)
        return curr.val if curr else -1

    def findMin(self, curr):
        while curr and curr.left:
            curr = curr.left
        return curr

    def getMax(self) -> int:
        curr = self.root

        while curr and curr.right:
            curr = curr.right

        return curr.val if curr else -1

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    # Move the node with key, return the new root of the subtree
    def removeHelper(self, curr: TreeNode, key: int) -> TreeNode:
        if not curr:
            return None

        if key < curr.key:
            curr.left = self.removeHelper(curr.left, key)

        elif key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        
        # Swap curr with inorder successor
        else:
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            else:
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)

        return curr
    
    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result

    def inorderTraversal(self, root: TreeNode, result: List[int]) -> None:
        if root:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)
        
