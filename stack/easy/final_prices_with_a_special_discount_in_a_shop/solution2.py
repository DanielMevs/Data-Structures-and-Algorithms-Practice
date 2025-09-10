from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """More space efficient than solution 1 as it does
         not store the value, just the index"""
        stack = [0]
        for i in range(1, len(prices)):
            curr = prices[i]
            while stack and prices[stack[-1]] >= curr:
                """The while loop indicates we want to apply the
                discount to all the eligible items, not just the
                most recent ones added to the stack"""
                idx = stack.pop()
                val = prices[idx]
                prices[idx] = val - curr
            stack.append(i)
        return prices
