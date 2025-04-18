from typing import List


class Solution:
    # Brute force solution (does not consider repeated queries)
    def vowelStrings(
            self, words: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for left, right in queries:
            count = 0
            for i in range(left, right + 1):
                if words[i][0] in vowels and words[i][-1] in vowels:
                    count += 1
            result.append(count)

        return result
