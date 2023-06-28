class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        count = 0
        i = 0

        while i < len(nums):
            while nums[i] == val:
                nums.pop(i)
                count += 1
                i -= 1
                    

            
            i += 1
            
        return count
        