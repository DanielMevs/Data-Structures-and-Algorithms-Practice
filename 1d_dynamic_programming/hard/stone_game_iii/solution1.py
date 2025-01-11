from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}

        # Return (alice - bob) or (bob - alice)
        def dfs(i):
            if i == len(stoneValue):
                return 0
            if i in dp:
                return dp[i]

            result = float('-inf')
            for j in range(i, min(i + 3, len(stoneValue))):
                result = max(result, sum(stoneValue[i: j + 1]) - dfs(j + 1))
            dp[i] = result
            return result

        return 'Alice' if dfs(0) > 0 else ('Bob' if dfs(0) < 0 else 'Tie')
