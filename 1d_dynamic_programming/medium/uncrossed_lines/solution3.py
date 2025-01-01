from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        prev = [0] * (len(nums2) + 1)
        for i in range(len(nums1)):
            dp = [0] * (len(nums2) + 1)

            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[j + 1] = prev[j] + 1
                else:
                    dp[j + 1] = max(
                        dp[j],
                        prev[j + 1]
                    )
            prev = dp

        return prev[-1]
