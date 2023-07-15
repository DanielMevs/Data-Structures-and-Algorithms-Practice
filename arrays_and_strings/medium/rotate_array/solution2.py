class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        temp = [None]*len(nums)
        for i in range(len(nums)):
            temp[i] = nums[(i-(k - 0))%len(nums)]
        for i in range(len(nums)):
            nums[i] = temp[i]
            