from collections import defaultdict, deque


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        # - Manager -> [list of employees]
        adj = defaultdict(list)

        for i in range(n):
            adj[manager[i]].append(i)

        # - BFS
        # - (id, time)
        queue = deque([(headID, 0)])
        result = 0

        while queue:
            i, time = queue.popleft()
            result = max(result, time)
            for emp in adj[i]:
                queue.append((emp, time + informTime[i]))

        return result