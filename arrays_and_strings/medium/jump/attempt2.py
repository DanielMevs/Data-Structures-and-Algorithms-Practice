class Solution:
    def canJump(self, nums: list[int]) -> bool:
        end = len(nums) -1
        if end < 1:
            return True

        for i, num in enumerate(nums):
            if i + num == end:
                return True
        return False