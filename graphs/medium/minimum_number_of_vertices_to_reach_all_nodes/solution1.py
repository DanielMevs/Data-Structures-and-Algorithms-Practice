from typing import List
from collections import defaultdict


class Solution:
    def findSmallestSetOfVertices(
            self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = defaultdict(list)
        for source, dest in edges:
            incoming[dest].append(source)

        result = []
        for i in range(n):
            if not incoming[i]:
                result.append(i)

        return result
