class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = {}

        def dfs(N, K):
            if N == K:
                return 1
            if N == 0 or K == 0:
                return 0
            if (N, K) in dp:
                return dp[(N, K)]

            dp[(N, K)] = (dfs(N - 1, K - 1) + (N - 1) * dfs(N - 1, K)) % MOD
            return dp[(N, K)]

        return dfs(n, k)
