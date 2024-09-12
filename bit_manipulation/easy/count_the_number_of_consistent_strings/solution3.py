from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        bit_mask = 0
        for c in allowed:
            bit_mask |= 1 << (ord(c) - 97)
        result = len(words)
        for word in words:
            for c in word:
                if not bit_mask & (1 << (ord(c) - 97)):
                    result -= 1
                    break

        return result
        