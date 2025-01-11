from typing import List


class Solution:
    # O(n * m^2) time complexity: n = len(words), m = max(len(word))
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        dp = {}

        def dfs(word):
            if word in dp:
                return dp[word]

            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if ((prefix in wordSet and suffix in wordSet) or
                        (prefix in wordSet and dfs(suffix))):
                    dp[word] = True
                    return dp[word]
            dp[word] = False
            return dp[word]

        result = []
        for word in words:
            if dfs(word):
                result.append(word)
        return result
