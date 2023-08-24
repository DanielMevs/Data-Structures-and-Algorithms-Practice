class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_min = prices[0]
        max_diff = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] < buy_min:
                buy_min = prices[i]
            
            diff = prices[i] - buy_min
            if diff > max_diff:
                max_diff = diff
        return max_diff