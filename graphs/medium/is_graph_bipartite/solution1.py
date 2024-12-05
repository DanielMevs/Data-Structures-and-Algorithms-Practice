from typing import List
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        odd = [0] * len(graph)  # Map node i -> odd=1, even=-1

        def bfs(i):
            if odd[i]:
                return True

            queue = deque([i])
            odd[i] = -1
            while queue:
                i = queue.popleft()
                for neighbor in graph[i]:
                    if odd[i] == odd[neighbor]:
                        return False
                    elif not odd[neighbor]:
                        queue.append(neighbor)
                        odd[neighbor] = -1 * odd[i]
            return True

        for i in range(len(graph)):
            if not bfs(i):
                return False

        return True
