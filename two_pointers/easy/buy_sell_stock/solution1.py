class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left, right = 0, 1 # left = buy; right = sell
        max_profit = 0

        while right < len(prices):
            # - Check profitability; we want buy to be
            # less than what we can sell it for.
            # - Notice that the left pointer stays fixed
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            
            right += 1

        return max_profit