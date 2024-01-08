class Solution:
    """
    @param nums: A list of integers
    @return: nothing
    """
    def wiggle_sort(self, nums: list[int]):
        for i in range(1, len(nums)):
            if ((i % 2 == 1 and nums[i] < nums[i - 1]) or
            (i % 2 == 0 and nums[i] > nums[i - 1])):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            
                
        return nums
