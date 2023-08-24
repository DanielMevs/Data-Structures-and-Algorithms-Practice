class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_min = prices[0]
        max_diff = 0
        n = len(prices)
        print(f'Current num: {buy_min}')
        print(f'Current min num: {buy_min}')
        print(f'Current max profit: {max_diff}')
        for i in range(1, n):
            print(f'Current num: {prices[i]}')
            
            if prices[i] < buy_min:
                buy_min = prices[i]
                print(f'Current min num: {buy_min}')
            else:
                diff = prices[i - 1] - buy_min
                if diff > max_diff:
                    max_diff = diff
                print(f'Current max profit: {max_diff}')

        return max_diff
    
test = Solution()
test.maxProfit(prices=[7,1,5,3,6,4])