from typing import List
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        while i != self.parent[i]:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i

    def union(self, a, b):
        aRoot = self.find(a)
        bRoot = self.find(b)

        if aRoot == bRoot:
            return False
        if self.rank[aRoot] < self.rank[bRoot]:
            self.parent[aRoot] = bRoot
            self.rank[bRoot] += self.rank[aRoot]
        else:
            self.parent[bRoot] = aRoot
            self.rank[aRoot] += self.rank[bRoot]
        return True


class Solution:
    '''
    Good path: starting node and ending node have same value and each node
    in the path has a value less than or equal to the starting node value.
    A single node can be considered a good path.
    '''
    def numberOfGoodPaths(
            self, vals: List[int], edges: List[List[int]]) -> int:
        adjacents = defaultdict(list)
        for a, b in edges:
            adjacents[a].append(b)
            adjacents[b].append(a)

        valToIndex = defaultdict(list)
        for i, val in enumerate(vals):
            valToIndex[val].append(i)

        result = 0
        uf = UnionFind(len(vals))
        for val in sorted(valToIndex.keys()):
            for i in valToIndex[val]:
                for neighbor in adjacents[i]:
                    if vals[neighbor] <= vals[i]:
                        uf.union(i, neighbor)

            # For each disjoint set, how many val's are in it
            count = defaultdict(int)
            for i in valToIndex[val]:
                count[uf.find(i)] += 1
                result += count[uf.find(i)]

        return result
