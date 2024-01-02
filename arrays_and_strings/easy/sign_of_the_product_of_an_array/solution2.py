class Solution:
    def arraySign(self, nums: list[int]) -> int:
        negatives = 0

        for num in nums:
            if num == 0:
                return 0
            negatives += (1 if num < 0 else 0)

        
        return -1 if negatives % 2 else 1
