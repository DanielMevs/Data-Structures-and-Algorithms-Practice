class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [0] * (target + 1)  # dp[i] = number of ways to roll i
        dp[0] = 1
        MOD = 10 ** 9 + 7

        for dice in range(n):
            next_dp = [0] * (target + 1)
            for val in range(1, k + 1):
                for total in range(val, target + 1):
                    next_dp[total] = (
                        next_dp[total] + dp[total - val]) % MOD
            dp = next_dp

        return dp[target]
