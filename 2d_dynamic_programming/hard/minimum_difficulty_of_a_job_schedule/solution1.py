from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        cache = {}

        def dfs(i, d, curr_max):
            if i == len(jobDifficulty):
                return 0 if d == 0 else float('inf')
            if d == 0:
                return float('inf')
            if (i, d, curr_max) in cache:
                return cache[(i, d, curr_max)]

            curr_max = max(curr_max, jobDifficulty[i])
            result = min(
                dfs(i + 1, d, curr_max),  # continue day
                curr_max + dfs(i + 1, d - 1, -1)  # end day
            )

            cache[(i, d, curr_max)] = result
            return result

        return dfs(0, d, 0)
