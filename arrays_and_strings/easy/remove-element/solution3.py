from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = 0
        i, j = 0, 0
        while i < len(nums):
            while i < len(nums) and nums[i] == val:
                i += 1
            if i < len(nums) and i > j:
                nums[j] = nums[i]
            result += 1 if i < len(nums) else 0
            i, j = i + 1, j + 1

        return result
