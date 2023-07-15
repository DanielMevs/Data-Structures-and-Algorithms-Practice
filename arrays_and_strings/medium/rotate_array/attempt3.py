class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        
        for i in range(len(nums)):
            temp = nums[i]
            nums[i] = nums[(i+k)%len(nums)]
            nums[(i+k)%len(nums)] = temp