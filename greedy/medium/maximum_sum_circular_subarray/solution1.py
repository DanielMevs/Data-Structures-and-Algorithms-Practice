from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax, globalMin = nums[0], nums[0]
        currentMax, currentMin = 0, 0
        total = 0

        for num in nums:
            currentMax = max(num, num + currentMax)
            currentMin = min(num, num + currentMin)
            globalMax = max(currentMax, globalMax)
            globalMin = min(currentMin, globalMin)
            total += num

        if globalMax < 0:
            return globalMax

        return max(total - globalMin, globalMax)
