from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        result = 0
        end = 0

        for interval in intervals:
            if interval[1] > end:
                result += 1
                end = interval[1]

        return result
