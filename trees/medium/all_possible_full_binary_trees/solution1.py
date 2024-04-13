# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode]:
        dp = {0: [], 1: [TreeNode()]}  # map n : list of full binary trees

        # - Return the list of full binary trees with n nodes
        def backtrack(n):
            
            if n in dp:
                return dp[n]
            
            result = []
            for left in range(n):  # 0 -> (n-1)
                right = n - 1 - left
                leftTrees, rightTrees = backtrack(left), backtrack(right)

                for tree1 in leftTrees:
                    for tree2 in rightTrees:
                        result.append(TreeNode(0, tree1, tree2))
            dp[n] = result
            return result
        
        return backtrack(n)