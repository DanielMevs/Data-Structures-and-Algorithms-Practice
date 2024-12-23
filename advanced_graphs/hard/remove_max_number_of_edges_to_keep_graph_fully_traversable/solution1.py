from typing import List


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    # Return 1 if success, 0 otherwise
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return 0
        if self.rank[p1] < self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.parent[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.parent[p1] = p2
        self.n -= 1
        return 1

    def isConnected(self):
        return self.n == 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice, bob = UnionFind(n), UnionFind(n)
        count = 0  # Number of edges we have to keep

        for t, src, dest in edges:
            if t == 3:
                count += (alice.union(src, dest) | bob.union(src, dest))

        for t, src, dest in edges:
            if t == 1:
                count += alice.union(src, dest)
            elif t == 2:
                count += bob.union(src, dest)

        if bob.isConnected() and alice.isConnected():
            return len(edges) - count

        return -1
