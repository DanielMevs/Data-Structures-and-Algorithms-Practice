from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> list[TreeNode]:
        subTrees = defaultdict(list)
        
        def dfs(node):
            if not node:
                return 'null'
            s = ', '.join([str(node.val), dfs(node.left), dfs(node.right)])
            if len(subTrees[s]) == 1:
                result.append(node)
            subTrees[s].append(node)
            return s
        
        result = []
        dfs(root)
        return result
            
            
        