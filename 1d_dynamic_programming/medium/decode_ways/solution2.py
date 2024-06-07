class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0
            
            result = dfs(i + 1)
            if (i + 1 < len(s) and (s[i] == '1' or
                                    s[i] == '2' and
                                    s[i + 1] in "0123456")):
                result += dfs(i + 2)
            dp[i] = result
            return result
        
        return dfs(0)