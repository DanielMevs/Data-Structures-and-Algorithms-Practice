class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp = {(len(s), True): 0, (len(s), False): 0}

        def dfs(i, mono):
            if (i, mono) in dp:
                return dp[(i, mono)]

            # All zeroes so far and s[i] == 0
            if mono and s[i] == '0':
                dp[(i, mono)] = min(1 + dfs(i + 1, mono=False),
                                    dfs(i + 1, mono))

            # All zeroes so far and s[i] == 1
            elif mono and s[i] == '1':
                dp[(i, mono)] = min(1 + dfs(i + 1, mono),
                                    dfs(i + 1, mono=False))

            # Not all zeroes so far and s[i] == 1
            elif not mono and s[i] == '1':
                dp[(i, mono)] = dfs(i + 1, mono)

            # Not all zeroes so far and s[i] == 0
            else:
                dp[(i, mono)] = 1 + dfs(i + 1, mono)

            return dp[(i, mono)]

        return dfs(0, True)
