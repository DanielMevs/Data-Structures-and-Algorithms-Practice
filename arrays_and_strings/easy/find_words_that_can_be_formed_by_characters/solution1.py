from typing import List
from collections import Counter, defaultdict


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        result = 0

        for word in words:
            current = defaultdict(int)
            good = True
            for char in word:
                current[char] += 1
                if char not in count or current[char] > count[char]:
                    good = False
                    break
            if good:
                result += len(word)
        
        return result