from typing import List
from collections import defaultdict


class Solution:
    def profitableSchemes(
            self, n: int, minProfit: int,
            group: List[int], profit: List[int]) -> int:
        mod = 10 ** 9 + 7
        dp = defaultdict(int)
        dp[(0, 0)] = 1

        for i in range(len(group)):
            next_dp = dp.copy()
            for (members, curr_profit), count in dp.items():
                new_members = members + group[i]
                new_profit = min(minProfit, curr_profit + profit[i])
                if new_members <= n:
                    next_dp[(new_members, new_profit)] = (
                        next_dp[(new_members, new_profit)] + count) % mod
            dp = next_dp

        return sum(dp[(m, minProfit)] for m, p in dp if p >= minProfit) % mod
