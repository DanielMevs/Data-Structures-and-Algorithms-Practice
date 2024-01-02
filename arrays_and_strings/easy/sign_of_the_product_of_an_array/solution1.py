class Solution:
    def arraySign(self, nums: list[int]) -> int:
        if 0 in nums:
            return 0
        negatives = 0
        for num in nums:
            if num < 0:
                negatives += 1
                
        return -1 if negatives % 2 == 1 else 1