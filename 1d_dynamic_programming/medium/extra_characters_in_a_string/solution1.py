from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        dp = {len(s): 0}

        def dfs(i):
            if i in dp:
                return dp[i]

            result = 1 + dfs(i + 1)  # skip current character
            for j in range(i, len(s)):
                if s[i: j + 1] in words:
                    result = min(result, dfs(j + 1))
            dp[i] = result
            return result

        return dfs(0)
