from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]

            cur_max = 0
            result = 0
            for j in range(i, min(len(arr), i + k)):
                cur_max = max(cur_max, arr[j])
                window_size = j - i + 1
                result = max(result, cur_max * window_size + dfs(j + 1))
            cache[i] = result
            return result

        return dfs(0)
