from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}

        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for neighbor in graph[i]:
                if not dfs(neighbor):
                    return safe[i]
            safe[i] = True
            return safe[i]

        result = []
        for i in range(n):
            if dfs(i):
                result.append(i)
        return result
