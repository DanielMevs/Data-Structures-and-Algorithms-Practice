from typing import List


class Solution:
    def profitableSchemes(
            self, n: int, minProfit: int,
            group: List[int], profit: List[int]) -> int:
        mod = 10 ** 9 + 7
        dp = {}

        def dfs(i, n, p):
            if i == len(group):
                return 1 if p >= minProfit else 0
            if (i, n, p) in dp:
                return dp[(i, n, p)]

            dp[(i, n, p)] = dfs(i + 1, n, p)  # skip i
            if n - group[i] >= 0:
                # include i
                dp[(i, n, p)] += dfs(i + 1, n - group[i], p + profit[i]) % mod

            return dp[(i, n, p)]

        return dfs(0, n, 0)
