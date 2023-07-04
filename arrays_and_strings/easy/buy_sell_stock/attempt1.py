class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        n = len(prices)
        for i in range(n - 1):
            if prices[i + 1] > prices[i]:
                diff = prices[i + 1] - prices[i]
                if diff > max_profit:
                    max_profit = diff
        return max_profit
    
test = Solution()
# Fails on:
test.maxProfit([7,1,5,3,6,4])