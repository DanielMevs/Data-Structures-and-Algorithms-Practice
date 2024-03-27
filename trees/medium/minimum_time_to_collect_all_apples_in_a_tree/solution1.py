class Solution:
    def minTime(self, n: int, edges: list[int], hasApple: list[bool]) -> int:
        adj = {i: [] for i in range(n)}
        for parent, child in edges:
            adj[parent].append(child)
            adj[child].append(parent)
        
        def dfs(current, parent):
            time = 0

            for child in adj[current]:
                if child == parent:
                    continue
                childTime = dfs(child, current)
                if childTime or hasApple[child]:
                    time += 2 + childTime
            return time
        
        return dfs(0, -1)