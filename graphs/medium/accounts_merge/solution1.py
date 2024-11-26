from typing import List
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parents[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parents[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAccount = {}  # email -> index of account

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAccount:
                    uf.union(i, emailToAccount[e])
                else:
                    emailToAccount[e] = i

        emailGroup = defaultdict(list)  # index of account -> list of emails
        for email, i in emailToAccount.items():
            leader = uf.find(i)
            emailGroup[leader].append(email)

        result = []
        for i in emailGroup.keys():
            name = accounts[i][0]
            result.append([name] + sorted(emailGroup[i]))  # arra concatenation

        return result
