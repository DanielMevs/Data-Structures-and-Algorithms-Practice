class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp_nums = nums
        for i in range(len(nums)):

            nums[i] = temp_nums[i-k]

        del temp_nums
        print(nums)

nums = [1,2,3,4,5,6,7]
k = 3

obj = Solution().rotate(nums, k)