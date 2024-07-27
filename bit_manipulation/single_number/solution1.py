from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0  # n ^ 0 = n
        for n in nums:
            result = n ^ result
        
        return result