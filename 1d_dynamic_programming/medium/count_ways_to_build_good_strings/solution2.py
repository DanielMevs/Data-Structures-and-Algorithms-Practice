class Solution:
    def countGoodStrings(
            self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = {0: 1}

        for i in range(1, high + 1):
            dp[i] = (dp.get(i - one, 0) + dp.get(i - zero, 0)) % mod

        return sum(dp[i] for i in range(low, high + 1)) % mod
