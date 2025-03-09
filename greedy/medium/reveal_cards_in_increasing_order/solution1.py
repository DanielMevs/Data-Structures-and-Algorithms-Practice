from typing import List
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        result = [0] * len(deck)
        queue = deque(range(len(deck)))

        for card in deck:
            i = queue.popleft()
            result[i] = card
            if queue:
                queue.append(queue.popleft())

        return result
