from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        left = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        return nums
