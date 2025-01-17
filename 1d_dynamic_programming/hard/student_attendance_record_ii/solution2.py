from collections import defaultdict


class Solution:
    # O(n) time complexity, O(1) space complexity
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 1:
            return 3

        result = {
            (0, 0): 1, (0, 1): 1, (0, 2): 0,
            (1, 0): 1, (1, 1): 0, (1, 2): 0
        }

        for _ in range(n - 1):
            temp = defaultdict(int)

            # Choose P
            temp[(0, 0)] = (
                (result[(0, 0)] + result[(0, 1)]) % MOD + result[(0, 2)]) % MOD
            temp[(1, 0)] = (
                (result[(1, 0)] + result[(1, 1)]) % MOD + result[(1, 2)]) % MOD

            # Choose L
            temp[(0, 1)] = result[(0, 0)]
            temp[(1, 1)] = result[(1, 0)]
            temp[(0, 2)] = result[(0, 1)]
            temp[(1, 2)] = result[(1, 1)]

            # Choose A
            temp[(1, 0)] = (temp[(1, 0)] + result[(0, 0)] % MOD) % MOD
            temp[(1, 0)] = (temp[(1, 0)] + result[(0, 1)] % MOD) % MOD
            temp[(1, 0)] = (temp[(1, 0)] + result[(0, 2)] % MOD) % MOD

            result = temp

        return sum(result.values()) % MOD
