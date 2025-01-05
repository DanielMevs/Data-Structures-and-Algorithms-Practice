class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        cache = {}

        # Start at score, return probability
        def dfs(score):
            if score >= k:
                return 1 if score <= n else 0

            if score in cache:
                return cache[score]

            prob = 0

            for i in range(1, maxPts + 1):
                prob += dfs(score + i)

            cache[score] = prob / maxPts
            return cache[score]

        return dfs(0)
