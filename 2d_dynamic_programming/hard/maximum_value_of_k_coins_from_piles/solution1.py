from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[-1] * (k + 1) for _ in range(n)]

        def dfs(i, coins):
            if i == n:
                return 0

            if dp[i][coins] != -1:
                return dp[i][coins]

            dp[i][coins] = dfs(i + 1, coins)  # skipping the current pile
            currentPile = 0

            for j in range(min(len(piles[i]), coins)):
                currentPile += piles[i][j]
                dp[i][coins] = \
                    max(dp[i][coins], currentPile + dfs(i + 1, coins - j - 1))

            return dp[i][coins]

        return dfs(0, k)
