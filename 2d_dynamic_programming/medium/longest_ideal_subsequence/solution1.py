class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        cache = {}

        def helper(i, prev):
            if i == len(s):
                return 0
            if (i, prev) in cache:
                return cache[(i, prev)]

            # skip s[i]
            result = helper(i + 1, prev)

            # include s[i]
            if prev == '' or abs(ord(s[i]) - ord(prev)) <= k:
                result = max(result, 1 + helper(i + 1, s[i]) + 1)

            cache[(i, prev)] = result
            return result

        return helper(0, '')
