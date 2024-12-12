from typing import List
from collections import defaultdict


class Solution:
    def minimumTime(
            self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adjacent = defaultdict(list)
        for source, dest in relations:
            adjacent[source].append(dest)

        max_time = {}  # source -> max_time

        def dfs(source):
            if source in max_time:
                return max_time[source]

            result = time[source - 1]
            for neighbor in adjacent[source]:
                result = max(result, time[source] + dfs(neighbor))
            max_time[source] = result
            return result

        for i in range(1, n + 1):
            dfs(i)

        return max(max_time.values())
