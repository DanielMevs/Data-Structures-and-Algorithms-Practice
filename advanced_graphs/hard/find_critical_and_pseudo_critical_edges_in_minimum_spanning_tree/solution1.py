from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, v1):
        while v1 != self.parent[v1]:
            self.parent[v1] = self.parent[self.parent[v1]]
            v1 = self.parent[v1]
        return v1

    def union(self, v1, v2):
        parent1, parent2 = self.find(v1), self.find(v2)

        if parent1 == parent2:
            return False

        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
            self.rank[parent1] += self.rank[parent2]

        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += self.rank[parent1]

        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(
            self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, edge in enumerate(edges):
            edge.append(i)  # [v1, v2, weight, original_index]
        edges.sort(key=lambda e: e[2])

        mst_weight = 0
        uf = UnionFind(n)
        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                mst_weight += w

        critical, pseudo_critical = [], []
        for n1, n2, e_weight, i in edges:
            # Try without current edge
            weight = 0
            uf = UnionFind(n)
            for v1, v2, w, j in edges:
                if i != j and uf.union(v1, v2):
                    weight += w
            if max(uf.rank) != n or weight > mst_weight:
                critical.append(i)
                continue

            # Try with current edge
            uf = UnionFind(n)
            uf.union(n1, n2)
            weight = e_weight
            for v1, v2, w, j in edges:
                if uf.union(v1, v2):
                    weight += w

            if weight == mst_weight:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]
