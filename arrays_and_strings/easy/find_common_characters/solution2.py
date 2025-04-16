from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])
        result = []

        for word in words[1:]:
            current = Counter(word)
            for c in count:
                # Current at c will default to 0 if missing
                count[c] = min(count[c], current[c])

        for letter, freq in count.items():
            result += [letter] * freq

        return result
