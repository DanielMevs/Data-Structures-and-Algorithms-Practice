from typing import List
from collections import defaultdict


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10 ** 9 + 7
        count = defaultdict(int)  # (index, char) -> count among all words

        for w in words:
            for i, c in enumerate(w):
                count[(i, c)] += 1

        dp = {}  # (i, k) -> number of ways to form target[:i]

        # i = index of target, k = index of words[j][k]
        def dfs(i, k):
            if i == len(target):
                return 1
            if k == len(words[0]):
                return 0
            if (i, k) in dp:
                return dp[(i, k)]

            c = target[i]
            dp[(i, k)] = dfs(i, k + 1)  # skip k position
            dp[(i, k)] += count[(k, c)] * dfs(i + 1, k + 1)  # use k position
            return dp[(i, k)] % mod

        return dfs(0, 0)
