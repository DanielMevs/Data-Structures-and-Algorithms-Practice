from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        two = nums[-1] == nums[-2]
        if len(nums) == 2:
            return two
        three = (
            nums[-1] == nums[-2] == nums[-3] or nums[-3] + 1
            == nums[-2] == nums[-1] - 1
        )

        dp = [three, two, False]
        for i in range(len(nums) - 4, -1, -1):
            current = (nums[i] == nums[i + 1]) and dp[1]
            current = current or (
                (nums[i] == nums[i + 1] == nums[i + 2] or
                    nums[i] + 1 == nums[i + 1] == nums[i + 2] - 1) and dp[2]
            )
            dp = [current, dp[0], dp[1]]

        return dp[0]
