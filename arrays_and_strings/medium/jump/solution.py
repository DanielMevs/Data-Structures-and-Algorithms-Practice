class Solution:
    def canJump(self, nums: list[int]) -> bool:
        end = len(nums) - 1
        if end < 1:
            return True
        max_jump = 0
        for i, num in enumerate(nums):
            if num == 0 and i == 0:
                return False
            if max_jump == 0 and num ==0:
                return False
            if num > max_jump:
                max_jump = num
            if i + num >= end and i != end:
                return True
            max_jump -= 1
        return False