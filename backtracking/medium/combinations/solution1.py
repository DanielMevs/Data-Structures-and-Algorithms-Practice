# - Runtime: k*(n!/((n-k)!*k!))

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []

        def backtrack(start, combination):
            if len(combination) == k:
                result.append(combination.copy())
                return
            
            for i in range(start, n + 1):
                combination.append(i)
                backtrack(i + 1, combination)
                combination.pop()
        
        backtrack(1, [])
        return result 