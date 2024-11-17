from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # start at city 0
        # recursively check its neighbors
        # count outgoing edges
        edges = {(a, b) for a, b in connections}
        neighbors = {city: [] for city in range(n)}
        visted = set()
        changes = 0

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            nonlocal edges, neighbors, visted, changes

            for neighbor in neighbors[city]:
                if neighbor in visted:
                    continue
                # Check if this neighbor can reach city 0
                if (neighbor, city) not in edges:
                    changes += 1
                visted.add(neighbor)
                dfs(neighbor)

        visted.add(0)
        dfs(0)
        return changes
