from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        minReach = [d / s for d, s in zip(dist, speed)]
        minReach.sort()
        minute = 0

        for timeReached in minReach:
            if minute < timeReached:
                minute += 1
            else:
                return minute
        return minute
