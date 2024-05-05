# - Runtime: O(2^t) where t = target

class Solution:
    def combinationSum(
            self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        # - Current = what numbers we have added to our current combination
        def dfs(i, current: list[int], total: int):
            if total == target:
                result.append(current.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            current.append(candidates[i])
            dfs(i, current, total + candidates[i])
            current.pop()
            dfs(i + 1, current, total)

        dfs(0, [], 0)
        return result