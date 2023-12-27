class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainder = {0: -1} # Mapping remainder to index
        total = 0

        for i, num in enumerate(nums):
            total += num
            current_remainder = total % k
            if current_remainder not in remainder:
                remainder[current_remainder] = i
            elif i - remainder[current_remainder] > 1:
                return True
        
        return False
            