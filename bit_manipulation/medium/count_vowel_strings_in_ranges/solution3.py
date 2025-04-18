from typing import List


class Solution:
    def vowelStrings(
            self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = sum(1 << (ord(c) - ord('a')) for c in 'aeiou')
        prefix = [0]

        for word in words:
            prefix += [prefix[-1]]
            if (
                1 << (ord(word[0]) - ord('a')) & vowels and
                1 << (ord(word[-1]) - ord('a')) & vowels
            ):
                prefix[-1] += 1

        return [prefix[right + 1] - prefix[left] for left, right in queries]
