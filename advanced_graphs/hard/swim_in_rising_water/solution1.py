from heapq import heappop, heappush


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        N = len(grid)
        visited = set()
        minHeap = [[grid[0][0], 0, 0]] # (time/max-height, r, c)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visited.add((0, 0))
        while minHeap:
            t, r, c = heappop(minHeap)
            visited.add((r, c))

            if r == N - 1 and c == N - 1:
                return t
            
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or
                    neiR == N or neiC == N or
                        (neiR, neiC) in visited):
                    continue
                visited.add((neiR, neiC))
                heappush(minHeap, [max(t, grid[neiR][neiC]), neiR, neiC])