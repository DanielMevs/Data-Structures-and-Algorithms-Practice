class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        mod = 10**9 + 7
        jumps = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [0, 3, 9],
            [],
            [0, 1, 7],
            [2, 6],
            [1, 3],
            [2, 4]
        ]

        dp = [1] * 10  # ways to land on i-th digit
        for _ in range(n - 1):
            new_dp = [0] * 10
            for i in range(10):
                for j in jumps[i]:
                    new_dp[j] += dp[i]
                    new_dp[j] %= mod
            dp = new_dp

        return sum(dp) % mod
