from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        result = [intervals[0]]

        for left, right in intervals[1:]:
            prev_left, prev_right = result[-1]
            if left > prev_left and right > prev_right:
                result.append([left, right])

        return len(result)
