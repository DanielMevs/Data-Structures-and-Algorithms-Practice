class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        cache = {}

        def helper(r, k):
            if k == len(key):
                return 0
            if (r, k) in cache:
                return cache[(r, k)]
            result = float('inf')

            for i, c in enumerate(ring):
                if c == key[k]:
                    min_dist = min(
                        abs(r - i),  # between
                        len(ring) - abs(r - i)  # around
                    )
                    result = min(
                        result,
                        min_dist + 1 + helper(i, k + 1)
                    )

            cache[((r, k))] = result
            return result

        return helper(0, 0)
