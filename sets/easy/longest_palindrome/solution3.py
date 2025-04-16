class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = set()
        result = 0

        for c in s:
            if c in letters:
                letters.remove(c)
                result += 2
            else:
                letters.add(c)

        return result + 1 if letters else result
