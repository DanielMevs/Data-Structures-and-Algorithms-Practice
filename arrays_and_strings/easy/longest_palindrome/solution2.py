from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        letters = defaultdict(int)

        for c in s:
            letters[c] += 1
            if letters[c] % 2 == 0:
                result += 2

        return result + (result < len(s))
