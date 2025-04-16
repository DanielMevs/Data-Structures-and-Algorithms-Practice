from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        first_word = Counter(words[0])
        words_count = [Counter(word) for word in words[1:]]
        result = []

        def is_letter_common(letter: str) -> bool:
            for word_count in words_count:
                if letter not in word_count:
                    return False
            return True

        def get_min_count(letter: str) -> int:
            running_min = first_word[letter]
            for word_count in words_count:
                running_min = min(running_min, word_count[letter])
            return running_min

        for letter in first_word:
            if is_letter_common(letter):
                for _ in range(get_min_count(letter)):
                    result.append(letter)

        return result
