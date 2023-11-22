class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            j = i - 1
            while j >= 0 and nums[j] > nums[j + 1]:
                temp = nums[j + 1]
                nums[j + 1] = nums[j]
                nums[j] = temp
                j -= 1
        return nums