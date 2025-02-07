from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        dp = {}

        def dfs(left, right):
            if right - left == 1:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]

            result = float('inf')
            for cut in cuts:
                if left < cut < right:
                    result = min(
                        result, (right - left) + (
                            dfs(left, cut) + dfs(cut, right))
                    )
            dp[(left, right)] = result = 0 if result == float('inf') \
                else result
            return result

        return dfs(0, n)
