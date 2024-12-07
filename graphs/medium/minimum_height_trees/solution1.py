from typing import List
from collections import defaultdict, deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adjacent = defaultdict(list)  # node -> [list of nodes]
        for n1, n2 in edges:
            adjacent[n1].append(n2)
            adjacent[n2].append(n1)

        leaves = deque()
        edge_count = {}
        for src, neighbors in adjacent.items():
            if len(neighbors) == 1:
                leaves.append(src)
            edge_count[src] = len(neighbors)

        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                leaf = leaves.popleft()
                n -= 1
                for neighbor in adjacent[leaf]:
                    edge_count[neighbor] -= 1
                    if edge_count[neighbor] == 1:
                        leaves.append(neighbor)
