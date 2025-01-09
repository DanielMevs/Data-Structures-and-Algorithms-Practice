from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * k
        dp[0] = arr[0]

        for i in range(1, len(arr)):
            curr_max = 0
            max_at_i = 0
            for j in range(i, i - k, -1):
                if j < 0:
                    break
                curr_max = max(curr_max, arr[j])
                window_size = i - j + 1
                curr_sum = curr_max * window_size
                sub_sum = dp[(j - 1) % k] if j - 1 >= 0 else 0
                max_at_i = max(max_at_i, curr_sum + sub_sum)

            dp[i % k] = max_at_i

        return dp[(len(arr) - 1) % k]
