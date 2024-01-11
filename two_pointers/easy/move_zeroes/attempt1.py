class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 1
        while right < len(nums):
            if nums[right] != 0 and nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1