from typing import List
from collections import defaultdict


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adjacent = defaultdict(list)  # node -> [list of nodes]
        for src, dest in edges:
            adjacent[src].append(dest)

        # Return max frequency of colors in a path
        def dfs(node):
            if node in path:
                return float('inf')
            if node in visited:
                return 0

            path.add(node)
            visited.add(node)

            colorIndex = ord(colors[node]) - ord('a')
            c[node][colorIndex] = 1
            for neighbor in adjacent[node]:
                if dfs(neighbor) == float('inf'):
                    return float('inf')
                for col in range(26):
                    c[node][col] = max(
                        c[node][col],
                        (1 if col == colorIndex else 0) + c[neighbor][col]
                    )

            path.remove(node)
            return max(c[node])

        result, n = 0, len(colors)
        visited, path = set(), set()
        c = [[0] * 26 for i in range(n)]  # Map count[node][color] -> max freq
        for node in range(n):
            result = max(result, dfs(node))

        return -1 if result == float('inf') else result
