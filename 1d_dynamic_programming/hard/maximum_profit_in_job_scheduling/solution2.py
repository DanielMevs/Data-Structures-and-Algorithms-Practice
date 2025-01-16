from typing import List
from bisect import bisect


class Solution:
    # O(nlogn) time complexity, O(n) space complexity
    def jobScheduling(
            self, startTime: List[int],
            endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]

            # don't include
            result = dfs(i + 1)

            # include
            j = bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = result = max(result, intervals[i][2] + dfs(j))
            return result

        return dfs(0)
