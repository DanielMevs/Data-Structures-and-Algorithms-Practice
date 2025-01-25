from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}

        def dfs(i, m, n):
            if i == len(strs):
                return 0
            if (i, m, n) in dp:
                return dp[(i, m, n)]

            mCount, nCount = strs[i].count("0"), strs[i].count("1")
            dp[(i, m, n)] = dfs(i + 1, m, n)
            if mCount <= m and nCount <= n:
                dp[(i, m, n)] = max(
                    1 + dfs(i + 1, m - mCount, n - nCount),
                    dfs(i, m, n)
                )
            return dp[(i, m, n)]

        return dfs(0, m, n)
