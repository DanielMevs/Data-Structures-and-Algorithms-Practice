class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        dp = {(1, 1): 1}

        for N in range(2, n + 1):
            for K in range(1, k + 1):
                dp[(N, K)] = (dp.get((N - 1, K - 1), 0) +
                              (N - 1) * dp.get((N - 1, K), 0))

        return dp[(n, k)] % (10 ** 9 + 7)
