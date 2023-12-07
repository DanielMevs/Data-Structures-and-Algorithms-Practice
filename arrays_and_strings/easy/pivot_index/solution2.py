class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        count = 0
        for i in range(len(nums)):
          if total - count - nums[i] == count:
            return i
          count += nums[i]
            
                 
        return -1
        