from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        balloon = Counter("balloon")

        result = float("inf")

        for char in balloon:
            result = min(result, countText[char] // balloon[char])
    
        return result