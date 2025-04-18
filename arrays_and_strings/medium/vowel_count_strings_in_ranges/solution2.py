from typing import List


class Solution:
    # Optimized solution using prefix sum (O(n) time complexity)
    def vowelStrings(
            self, words: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        vowels = {'a', 'e', 'i', 'o', 'u'}
        prefix_sum = [0] * (len(words) + 1)

        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i - 1] + (
                words[i - 1][0] in vowels and
                words[i - 1][-1] in vowels
            )

        for start, end in queries:
            count = prefix_sum[end + 1] - prefix_sum[start]
            result.append(count)

        return result
