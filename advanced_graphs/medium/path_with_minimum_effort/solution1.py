from typing import List
from heapq import heappush, heappop


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        minHeap = [[0, 0, 0]]  # [difference, r, c]
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while minHeap:
            diff, r, c = heappop(minHeap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if (r, c) == (ROWS - 1, COLS - 1):
                return diff

            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if (newR < 0 or newC < 0 or
                        newR == ROWS or newC == COLS or
                        (newR, newC) in visited):
                    continue
                newDiff = max(diff, abs(heights[r][c] - heights[newR][newC]))
                heappush(minHeap, [newDiff, newR, newC])
