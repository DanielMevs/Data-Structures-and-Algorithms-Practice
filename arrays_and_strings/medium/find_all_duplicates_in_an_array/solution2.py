# Efficient solution using O(1) space and O(n) time complexity
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            num = abs(num)
            if nums[num - 1] < 0:
                result.append(num)
            else:
                nums[num - 1] *= -1
        
        return result