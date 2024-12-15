from typing import List
from collections import deque
from heapq import heappush, heappop


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        def in_bounds(r, c):
            return min(r, c) >= 0 and max(r, c) < n

        def preCompute():
            thieves = deque()
            min_distance = {}
            for r in range(n):
                for c in range(n):
                    if grid[r][c]:
                        thieves.append([r, c, 0])
                        min_distance[(r, c)] = 0
            while thieves:
                r, c, distance = thieves.popleft()
                neighbors = [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]

                for r2, c2 in neighbors:
                    if in_bounds(r2, c2) and (r2, c2) not in min_distance:
                        min_distance[(r2, c2)] = distance + 1
                        thieves.append([r2, c2, distance + 1])

            return min_distance

        min_distance = preCompute()
        maxHeap = [(-min_distance[(0, 0)], 0, 0)]  # (dist, r, c)
        visited = set()
        visited.add((0, 0))

        while maxHeap:
            dist, r, c = heappop(maxHeap)
            dist = -dist
            if (r, c) == (n - 1, n - 1):
                return dist
            neighbors = [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]
            for r2, c2 in neighbors:
                if in_bounds(r2, c2) and (r2, c2) not in visited:
                    visited.add((r2, c2))
                    dist2 = min(dist, min_distance[(r2, c2)])
                    heappush(maxHeap, (-dist2, r2, c2))
