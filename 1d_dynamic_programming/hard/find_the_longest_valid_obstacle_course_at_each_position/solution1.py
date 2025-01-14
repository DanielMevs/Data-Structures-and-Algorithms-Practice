from typing import List
from bisect import bisect


class Solution:
    def longestObstacleCourseAtEachPosition(
            self, obstacles: List[int]) -> List[int]:
        # result[i] = height of LIS ending at i & including obstacles[i]
        result = []

        # dp[i], where i = length of LIS, is the smallest ending value
        dp = [10**8] * (len(obstacles) + 1)

        for num in obstacles:
            index = bisect(dp, num)
            result.append(index + 1)
            dp[index] = num

        return result
