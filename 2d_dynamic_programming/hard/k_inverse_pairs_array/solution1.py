class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        cache = {}  # (n, k) -> count

        def count(n, k):
            if n == 0:
                return 1 if k == 0 else 0
            if k < 0:
                return 0
            if (n, k) in cache:
                return cache[(n, k)]

            cache[(n, k)] = 0
            for i in range(n):
                cache[(n, k)] = (
                    (cache[n, k] + count(n - 1, k - i)) % MOD
                )

            return cache[(n, k)]

        return count(n, k)
