class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7
        dp = {}

        def dfs(i, steps):
            if steps == 0:
                return i == 0
            if (i, steps) in dp:
                return dp[(i, steps)]

            result = dfs(i, steps - 1)
            if i > 0:
                result = (result + dfs(i - 1, steps - 1)) % mod
            if i < arrLen - 1:
                result = (result + dfs(i + 1, steps - 1)) % mod

            dp[(i, steps)] = result
            return result

        return dfs(0, steps)
