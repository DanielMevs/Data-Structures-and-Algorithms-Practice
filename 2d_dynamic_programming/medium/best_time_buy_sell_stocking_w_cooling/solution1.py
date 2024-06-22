class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If sell -> i + 2

        cache = {}  # key=(i, buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            # - If we have already encountered this case, return the
            # already-computed value.
            if (i, buying) in cache:
                return cache[(i, buying)]
            
            cool_down = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cache[(i, buying)] = max(buy, cool_down)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                cache[(i, buying)] = max(sell, cool_down)
            
            return cache[(i, buying)]
        
        return dfs(0, True)