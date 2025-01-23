from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}  # subarr piles (l, r) -> Max Alice Total

        # Return: Max Alice Total
        def dfs(left, right):
            if left > right:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]

            even = True if (right - left) % 2 else False
            leftChoice = piles[left] if even else 0
            rightChoice = piles[right] if even else 0

            dp[(left, right)] = max(
                dfs(left + 1, right) + leftChoice,
                dfs(left, right - 1) + rightChoice
            )

            return dp[(left, right)]

        return dfs(0, len(piles) - 1) > (sum(piles) // 2)
