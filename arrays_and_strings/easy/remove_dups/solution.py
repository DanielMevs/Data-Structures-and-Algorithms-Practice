class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_nums = []
        for num in list(nums):
            if num not in unique_nums:
                unique_nums.append(num)
        k = len(unique_nums)
        return k