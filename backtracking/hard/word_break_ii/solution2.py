from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)

        def backtrack(i):
            if i == len(s):
                return [""]

            result = []
            for j in range(i, len(s)):
                word = s[i: j + 1]
                if word not in wordDict:
                    continue
                strings = backtrack(j + 1)
                if not strings:
                    continue
                for subStr in strings:
                    sentence = word
                    if subStr:
                        sentence += " " + subStr
                    result.append(sentence)
            return result

        return backtrack(0)
