from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left, right = 0, len(cardPoints) - k
        result = total = sum(cardPoints[right:])

        while right < len(cardPoints):
            total += cardPoints[left] - cardPoints[right]
            result = max(result, total)
            left, right = left + 1, right + 1

        return result
