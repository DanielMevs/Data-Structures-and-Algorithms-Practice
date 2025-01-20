class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * (len(s) + 1) for i in range(len(s) + 1)]
        result = 0

        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                if s[i] == s[j]:
                    dp[i][j] = 1 if i == j else 2
                    if i - 1 >= 0:
                        dp[i][j] += dp[i - 1][j + 1]
                else:
                    dp[i][j] = dp[i][j + 1]
                    if i - 1 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j])

                result = max(result, dp[i][j])

        return result
