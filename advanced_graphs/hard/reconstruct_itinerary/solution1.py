class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adjacent = {source: [] for source, dest in tickets}
        result = []
        
        tickets.sort()
        for src, dst in tickets:
            adjacent[src].append(dst)
        
        for key in adjacent:
            adjacent[key].sort()
        
        def dfs(adj, result, src):
            if src in adj:
                destinations = adj[src][:]
                while destinations:
                    dest = destinations[0]
                    adj[src].pop(0)
                    dfs(adj, result, dest)
                    destinations = adj[src][:]
            result.append(src)
           
        dfs(adjacent, result, "JFK")
        result.reverse()

        if len(result) != len(tickets) + 1:
            return []
        
        return result