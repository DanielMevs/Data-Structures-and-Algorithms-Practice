class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums