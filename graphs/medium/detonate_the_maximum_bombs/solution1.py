from typing import List
from collections import defaultdict
from math import sqrt


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adjacent = defaultdict(list)  # bomb -> [list of bombs]

        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

                if dist <= r1:
                    adjacent[i].append(j)
                if dist <= r2:
                    adjacent[j].append(i)

        def dfs(i, visited):
            if i in visited:
                return 0
            visited.add(i)
            for neighbor in adjacent[i]:
                dfs(neighbor, visited)
            return len(visited)

        result = 0
        for i in range(len(bombs)):
            result = max(result, dfs(i, set()))

        return result
