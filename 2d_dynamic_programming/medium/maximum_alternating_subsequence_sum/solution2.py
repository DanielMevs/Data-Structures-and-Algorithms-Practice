from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sumEven, sumOdd = 0, 0
        for i in range(len(nums) - 1, -1, -1):
            tempEven = max(sumEven, sumOdd + nums[i])
            tempOdd = max(sumOdd, sumEven - nums[i])
            sumEven, sumOdd = tempEven, tempOdd
        return sumEven
