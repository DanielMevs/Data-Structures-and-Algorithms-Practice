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
          
    def helper(self, left, right, nums):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1
        