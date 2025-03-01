from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Calculate the difference in cost for each city B and city A
        costDiffs = sorted(costs, key=lambda x: x[1] - x[0])
        totalCost = 0
        n = len(costs) // 2

        # Select the first n cities with the smallest difference for city B
        for i in range(n):
            totalCost += costDiffs[i][1]

        # Select the remaining n cities for city A
        for i in range(n, len(costs)):
            totalCost += costDiffs[i][0]

        return totalCost
