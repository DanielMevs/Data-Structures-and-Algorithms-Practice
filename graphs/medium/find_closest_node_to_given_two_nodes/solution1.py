from typing import List
from collections import deque, defaultdict


class Solution:
    def closestMeetingNode(
            self, edges: List[int], node1: int, node2: int) -> int:
        adjacent = defaultdict(list)
        for i, destination in enumerate(edges):
            adjacent[i].append(destination)

        def bfs(src, distMap):
            queue = deque()
            queue.append([src, 0])
            distMap[src] = 0
            while queue:
                node, dist = queue.popleft()
                for neighbor in adjacent[node]:
                    if neighbor not in distMap:
                        queue.append([neighbor, dist + 1])
                        distMap[neighbor] = dist + 1

        node1Dist = {}  # Map node -> distance from node1
        node2Dist = {}  # Map node -> distance from node2
        bfs(node1, node1Dist)
        bfs(node2, node2Dist)

        result = -1
        resultDist = float('inf')
        for i in range(len(edges)):
            if i in node1Dist and i in node2Dist:
                dist = max(node1Dist[i], node2Dist[i])
                if dist < resultDist:
                    result = i
                    resultDist = dist
        return result
