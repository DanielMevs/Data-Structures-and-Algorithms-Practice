class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left, right = 0 ,1

        while right < len(nums):
            if nums[right] != 0 and nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right + 1
            elif nums[right] == 0 and nums[left] == 0:
                right += 1
            else:
                left, right = left + 1, right + 1
        

            