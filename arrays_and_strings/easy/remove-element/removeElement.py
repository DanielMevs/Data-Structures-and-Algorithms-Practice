class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        i = 0
        for num in nums:
            if num == val:
                nums.pop(i)
                i += 1
                count += 1
            else:
                i +=1
        return count
