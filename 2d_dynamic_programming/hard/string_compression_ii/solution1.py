class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        cache = {}

        def count(i, k, prev, prev_count):
            if (i, k, prev, prev_count) in cache:
                return cache[(i, k, prev, prev_count)]
            if k < 0:
                return float('inf')
            if i == len(s):
                return 0

            if s[i] == prev:
                inc = 1 if prev_count in [1, 9, 99] else 0
                result = inc + count(i + 1, k, prev, prev_count + 1)
            else:
                result = min(   
                    count(i + 1, k - 1, prev, prev_count),  # delete s[i]
                    1 + count(i + 1, k, s[i], 1)  # don't delete s[i]
                )

            cache[(i, k, prev, prev_count)] = result
            return result

        return count(0, k, None, 0)
