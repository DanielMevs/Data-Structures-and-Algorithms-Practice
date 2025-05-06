from collections import Counter, defaultdict
from typing import List


class Solution:
    def wordSubsets(
            self, words1: List[str], words2: List[str]) -> List[str]:
        max_count = defaultdict(int)
        for word in words2:
            current = Counter(word)
            for letter in current:
                max_count[letter] = max(max_count[letter], current[letter])

        result = []
        for word in words1:
            current = Counter(word)
            if all(
                    current[letter] >= max_count[letter]
                    for letter in max_count):
                result.append(word)

        return result
