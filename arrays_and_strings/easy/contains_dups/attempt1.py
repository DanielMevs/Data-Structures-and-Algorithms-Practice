# naive approach

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            if nums[i] in nums[:i]:
                return True