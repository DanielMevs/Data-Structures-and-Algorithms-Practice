from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda w: -len(w))
        word_index = {w: i for i, w in enumerate(words)}  # word -> index

        dp = {}  # index -> longest chain

        def dfs(i):
            if i in dp:
                return dp[i]
            result = 1

            w = words[i]
            for j in range(len(words[i])):
                pred = w[:j] + w[j + 1:]
                if pred in word_index:
                    result = max(result, 1 + dfs(word_index[pred]))

            dp[i] = result
            return result

        for i in range(len(words)):
            dfs(i)

        return max(dp.values())
