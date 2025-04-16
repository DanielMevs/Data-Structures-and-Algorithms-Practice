from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = defaultdict(int)
        result = max_odd = 0

        for letter in s:
            letters[letter] += 1

        for count in letters.values():
            if count % 2 == 0:
                result += count
            elif count > max_odd:
                result += max_odd - 1 if max_odd else 0
                max_odd = count
            else:
                result += count - 1

        return result + max_odd
