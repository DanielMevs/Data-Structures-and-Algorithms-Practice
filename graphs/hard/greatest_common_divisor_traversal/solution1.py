from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.size[px] < self.size[py]:
            self.parent[px] = py
            self.size[py] += self.size[px]
        else:
            self.parent[py] = px
            self.size[px] += self.size[py]
        self.count -= 1


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))
        factor_index = {}  # f -> index of value with factor f
        for i, num in enumerate(nums):
            f = 2
            while f * f <= num:
                if num % f == 0:
                    if f in factor_index:
                        uf.union(i, factor_index[f])
                    else:
                        factor_index[f] = i
                    while num % f == 0:
                        num //= f
                f += 1
            if num > 1:
                if num in factor_index:
                    uf.union(i, factor_index[num])
                else:
                    factor_index[num] = i

        return uf.count == 1
