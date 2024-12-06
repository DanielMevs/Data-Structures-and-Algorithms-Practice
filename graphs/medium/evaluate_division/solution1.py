from typing import List
from collections import defaultdict, deque


class Solution:
    def calcEquation(
            self, equations: List[List[str]],
            values: List[float], queries: List[List[str]]) -> List[float]:
        adjacent = defaultdict(list)  # Map a -> list of [b, a/b]
        for i, eq in enumerate(equations):
            a, b = eq
            adjacent[a].append([b, values[i]])
            adjacent[b].append([a, 1 / values[i]])

        def bfs(src, target):
            if src not in adjacent or target not in adjacent:
                return -1.0
            queue, visited = deque(), set()
            queue.append([src, 1.0])
            visited.add(src)
            while queue:
                node, weight = queue.popleft()
                if node == target:
                    return weight
                for neighbor, w in adjacent[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append([neighbor, weight * w])
            return -1

        return [bfs(q[0], q[1]) for q in queries]
