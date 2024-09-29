from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        left = result = 0

        for right in range(1, len(colors)):
            if colors[left] == colors[right]:
                if neededTime[left] < neededTime[right]:
                    result += neededTime[left]
                    left = right
                else:
                    result += neededTime[right]
            else:
                left = right
        
        return result