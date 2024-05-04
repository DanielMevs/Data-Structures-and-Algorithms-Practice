class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        subset = []
        
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            # - Descision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # - Decision to NOT include nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return result