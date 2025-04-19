from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        indices = list(range(len(heights)))
        indices.sort(key=lambda i: -heights[i])
        return [names[i] for i in indices]
