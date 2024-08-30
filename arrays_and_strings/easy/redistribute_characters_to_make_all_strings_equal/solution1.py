from typing import List
from collections import defaultdict


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_count = defaultdict(int)

        for word in words:
            for char in word:
                char_count[char] += 1
        
        for char in char_count:
            if char_count[char] % len(words):
                return False
        
        return True