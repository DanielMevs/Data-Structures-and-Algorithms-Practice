from typing import List
from collections import Counter


class Solution:
    def maxScoreWords(
            self, words: List[str],
            letters: List[str],
            score: List[int]) -> int:
        def can_form_word(word, letter_count):
            word_count = Counter(word)
            for char in word_count:
                if word_count[char] > letter_count[char]:
                    return False
            return True

        def get_score(word):
            result = 0
            for char in word:
                result += score[ord(char) - ord('a')]
            return result

        letter_count = Counter(letters)

        def backtrack(i):
            if i == len(words):
                return 0
            result = backtrack(i + 1)  # skip
            # include (when possible)
            if can_form_word(words[i], letter_count): 
                for char in words[i]:
                    letter_count[char] -= 1
                result = max(result, get_score(words[i]) + backtrack(i + 1))
                for char in words[i]:
                    letter_count[char] += 1

            return result

        return backtrack(0)
