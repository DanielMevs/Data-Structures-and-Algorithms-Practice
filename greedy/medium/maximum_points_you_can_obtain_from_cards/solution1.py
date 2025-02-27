from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        windowSize = n - k
        # minSum -> the minimum sum of the current window
        minSum = currentSum = sum(cardPoints[:windowSize])

        for i in range(windowSize, n):
            currentSum += cardPoints[i] - cardPoints[i - windowSize]

            minSum = min(minSum, currentSum)

        return sum(cardPoints) - minSum
