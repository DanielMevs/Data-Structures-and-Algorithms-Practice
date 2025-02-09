class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7
        arrLen = min(steps, arrLen)
        dp = [0] * arrLen
        dp[0] = 1

        for steps in range(1, steps + 1):
            next_dp = [0] * arrLen
            for i in range(arrLen):
                next_dp[i] = dp[i]
                if i > 0:
                    next_dp[i] = dp[i]
                if i > 0:
                    next_dp[i] = (next_dp[i] + dp[i - 1]) % mod
                if i < arrLen - 1:
                    next_dp[i] = (next_dp[i] + dp[i + 1]) % mod

            dp = next_dp

        return dp[0]
