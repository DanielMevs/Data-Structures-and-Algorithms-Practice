from typing import List


class Solution:
    # O(N^2) time complexity, O(N) space complexity
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

            j = i + 1
            while j < len(intervals):
                if intervals[i][1] <= intervals[j][0]:
                    break
                j += 1

            # include
            cache[i] = result = max(result, intervals[i][2] + dfs(j))
            return result

        return dfs(0)
