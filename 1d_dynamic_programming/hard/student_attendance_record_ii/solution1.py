from collections import defaultdict


class Solution:
    # O(n) time complexity, O(1) space complexity
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        cache = {}

        def count(n):
            if n == 1:
                # (A, L)
                return {(0, 0): 1, (0, 1): 1, (0, 2): 0,
                        (1, 0): 1, (1, 1): 0, (1, 2): 0}

            if n in cache:
                return cache[n]

            temp = count(n - 1)
            result = defaultdict(int)

            # Choose P
            result[(0, 0)] = (
                (temp[(0, 0)] + temp[(0, 1)]) % MOD + temp[(0, 2)]) % MOD
            result[(1, 0)] = (
                (temp[(1, 0)] + temp[(1, 1)]) % MOD + temp[(1, 2)]) % MOD

            # Choose L
            result[(0, 1)] = temp[(0, 0)]
            result[(1, 1)] = temp[(1, 0)]
            result[(0, 2)] = temp[(0, 1)]
            result[(1, 2)] = temp[(1, 1)]

            # Choose A
            result[(1, 0)] = (result[(1, 0)] + temp[(0, 0)] % MOD) % MOD
            result[(1, 0)] = (result[(1, 0)] + temp[(0, 1)] % MOD) % MOD
            result[(1, 0)] = (result[(1, 0)] + temp[(0, 2)] % MOD) % MOD

            cache[n] = result

            return result

        return sum(count(n).values()) % MOD
