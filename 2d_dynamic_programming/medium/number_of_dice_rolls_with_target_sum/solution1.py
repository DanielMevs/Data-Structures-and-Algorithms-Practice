class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        cache = {}  # (n, target) -> count

        def count(n, target):
            if n == 0:
                return 1 if target == 0 else 0
            if (n, target) in cache:
                return cache[(n, target)]
            result = 0
            for val in range(1, k + 1):
                result = (result + count(n - 1, target - val)) % MOD
            cache[(n, target)] = result
            return result

        return count(n, target)
