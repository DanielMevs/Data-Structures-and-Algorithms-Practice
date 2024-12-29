from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # Dynamic programming

        dp = {}  # key = index, value = [length of LIS, count]
        lenLIS, result = 0, 0  # length of LIS, count of LIS

        # i = start of subseq
        for i in range(len(nums) - 1, -1, -1):
            maxLen, maxCount = 1, 1  # len, count of LIS start from i

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    length, count = dp[j]
                    if length + 1 > maxLen:
                        maxLen, maxCount = length + 1, count
                    elif length + 1 == maxLen:
                        maxCount += count

            if maxLen > lenLIS:
                lenLIS, result = maxLen, maxCount
            elif maxLen == lenLIS:
                result += maxCount
            dp[i] = [maxLen, maxCount]

        return result
