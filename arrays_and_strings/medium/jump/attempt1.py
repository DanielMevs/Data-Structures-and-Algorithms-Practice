class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums)
        if end == 1:
            return True

        for i, num in enumerate(nums):
            if i + num == end:
                return True
        return False