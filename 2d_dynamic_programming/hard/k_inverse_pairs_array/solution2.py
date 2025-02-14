class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        prev = [0] * (k + 1)
        prev[0] = 1

        for N in range(1, n + 1):
            current = [0] * (k + 1)
            for K in range(k + 1):
                for pairs in range(N):
                    current[K] += prev[K - pairs] if K - pairs >= 0 else 0
                    current[K] %= MOD
            prev = current

        return prev[k]
