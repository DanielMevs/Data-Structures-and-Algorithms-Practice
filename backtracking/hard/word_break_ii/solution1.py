from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)

        def backtrack(i):
            if i == len(s):
                result.append(' '.join(current))
                return
            for j in range(i, len(s)):
                word = s[i: j + 1]
                if word in wordDict:
                    current.append(word)
                    backtrack(j + 1)
                    current.pop()

        current = []
        result = []
        backtrack(0)
        return result
