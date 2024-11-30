from typing import List
from collections import defaultdict


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adjacent = defaultdict(list)  # map node -> list of (neighbor, dist)
        for source, destination, distance in roads:
            adjacent[source].append((destination, distance))
            adjacent[destination].append((source, distance))

        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            nonlocal result
            for neighbor, distance in adjacent[i]:
                result = min(result, distance)
                dfs(neighbor)

        result = float('inf')
        visited = set()
        dfs(1)
        return result
