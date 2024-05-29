from heapq import heappop, heappush


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}  # i: list of [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        # Prim's
        result = 0
        visited = set()
        minHeap = [[0, 0]]  # [cost, point]
        while len(visited) < N:
            cost, i = heappop(minHeap)
            if i in visited:
                continue
            result += cost
            visited.add(i)
            for neighborCost, neighbor in adj[i]:
                if neighbor not in visited:
                    heappush(minHeap, [neighborCost, neighbor])
        
        return result