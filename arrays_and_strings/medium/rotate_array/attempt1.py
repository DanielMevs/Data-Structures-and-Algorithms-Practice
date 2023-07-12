class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp_nums = nums
        for i in range(len(nums)):
            nums[i] = temp_nums[i-k]


