from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    # Time complexity: O(E * log(V))
    def maxProbability(
            self, n: int, edges: List[List[int]],
            succProb: List[float], start_node: int,
            end_node: int) -> float:

        adjacent = defaultdict(list)
        for i in range(len(edges)):
            src, dist = edges[i]
            adjacent[src].append((dist, succProb[i]))
            adjacent[dist].append((src, succProb[i]))

        priority_queue = [(-1, start_node)]
        visited = set()

        while priority_queue:
            probability, current = heappop(priority_queue)
            visited.add(current)

            if current == end_node:
                return -probability
            for neighbor, edge_probability in adjacent[current]:
                if neighbor in visited:
                    continue
                heappush(
                    priority_queue, (probability * edge_probability, neighbor))

        return 0
