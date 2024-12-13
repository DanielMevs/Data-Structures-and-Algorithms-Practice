from typing import List
from collections import defaultdict


class Solution:
    def findAllPeople(
            self, n: int, meetings: List[List[int]],
            firstPerson: int) -> List[int]:

        secrets = set([0, firstPerson])  # people with secret
        time_map = {}

        for src, dest, time in meetings:
            if time not in time_map:
                time_map[time] = defaultdict(list)
            time_map[time][src].append(dest)
            time_map[time][dest].append(src)

        def dfs(src, adjacent):
            if src in visited:
                return
            visited.add(src)
            secrets.add(src)
            for neighbor in adjacent[src]:
                dfs(neighbor, adjacent)

        for time in sorted(list(time_map.keys())):
            visited = set()
            for src in time_map[time]:
                if src in secrets:
                    dfs(src, time_map[time])

        return list(secrets)
