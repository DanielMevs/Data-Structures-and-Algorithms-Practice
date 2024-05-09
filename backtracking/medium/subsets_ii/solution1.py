class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                result.append(subset[::])
                return
            
            # - All subsets that include nums[i] / left subtree
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # - All subsets that don't include nums[i] / right subtree
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, subset)
        
        backtrack(0, [])
        return result