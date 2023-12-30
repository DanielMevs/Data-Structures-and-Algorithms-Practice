class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        while i < len(nums):
            num = nums[i]
            if num == val:
                nums[i] = nums[-1]
                nums.pop()
            if i < len(nums) and nums[i] == val:
                i -= 1
            i += 1
            
        
        
        return len(nums)