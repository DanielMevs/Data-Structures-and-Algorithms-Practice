from typing import List
from collections import defaultdict
from math import ceil


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adjacent = defaultdict(list)
        for source, destination in roads:
            adjacent[source].append(destination)
            adjacent[destination].append(source)

        def dfs(node, parent):
            nonlocal result
            passengers = 0
            for child in adjacent[node]:
                if child != parent:
                    passenger = dfs(child, node)
                    passengers += passenger
                    result += int(ceil(passenger / seats))
            return passengers + 1

        result = 0
        dfs(0, -1)
        return result
