class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        temp = [None]*len(nums)
        for i in range(len(nums)):

            temp[i] = nums[(i+k)%len(nums)]
        nums = temp

obj = Solution().rotate([1,2,3,4,5,6,7], 3)
