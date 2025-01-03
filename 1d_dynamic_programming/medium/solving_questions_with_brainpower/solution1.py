from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # O(n) time complexity, O(n) space complexity

        dp = {}

        def dfs(i):
            if i >= len(questions):
                return 0

            if i in dp:
                return dp[i]

            dp[i] = max(
                dfs(i + 1),  # Skip the current question
                questions[i][0] + dfs(i + 1 + questions[i][1])  # Solve current
            )
            return dp[i]

        return dfs(0)
