class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            value = abs(nums[i])
            if 1 <= value <= len(nums):
                if nums[value - 1] > 0:
                    nums[value - 1] *= -1
                elif nums[value - 1] == 0:
                    nums[value - 1] = (len(nums) + 1) * -1
        
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        
        return len(nums) + 1