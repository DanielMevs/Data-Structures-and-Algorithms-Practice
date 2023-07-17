class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) -1
        if end < 1:
            return True
        count = 1
        for i, num in enumerate(nums):
            count -= 1
            if num == 0 and i == 0:
                return False
            if count == 0:
                return False
            if i + num >= end and i != end:
                return True
            count += num
        return False