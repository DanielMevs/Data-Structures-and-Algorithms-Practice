from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = 0
        i, j = 0, 0
        while i < len(nums):
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            if i < len(nums) - 1 and i > j:
                nums[j + 1] = nums[i + 1]
            result += 1
            i, j = i + 1, j + 1

        return result
