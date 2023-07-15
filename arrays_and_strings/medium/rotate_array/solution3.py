class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        k = k % len(nums)
        l, r = 0, len(nums) - 1
        self.helper(l, r, nums)
        l, r = 0, k - 1
        self.helper(l, r, nums)
        l, r = k, len(nums) - 1
        self.helper(l, r, nums)
        
        
    def helper(self, l, r, nums):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        