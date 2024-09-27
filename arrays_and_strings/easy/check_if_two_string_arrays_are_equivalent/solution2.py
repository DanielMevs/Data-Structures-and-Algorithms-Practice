from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = w2 = 0  # - Index of word
        i = j = 0  # - Index of character in word

        while w1 < len(word1) and w2 < len(word2):
            if word1[w1][i] != word2[w2][j]:
                return False

            i, j = i + 1, j + 1

            if i == len(word1[w1]):
                i = 0
                w1 += 1

            if j == len(word2[w2]):
                j = 0
                w2 += 1
        
        return w1 == len(word1) and w2 == len(word2)