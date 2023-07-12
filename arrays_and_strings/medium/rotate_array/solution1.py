class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        import copy
        if len(nums) == 1:
            return
        temp_nums = copy.deepcopy(nums)
        for i in range(len(nums)):

            nums[i] = temp_nums[(i-k)%len(nums)]

        del temp_nums