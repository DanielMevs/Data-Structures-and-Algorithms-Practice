from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_chars = set(allowed)
        count = 0
        for word in words:
            is_consistent = True
            for letter in word:
                if letter not in allowed_chars:
                    is_consistent = False
            count += 1 if is_consistent else 0

        return count
