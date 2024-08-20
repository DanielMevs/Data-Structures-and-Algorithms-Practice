from typing import List
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        result = 0
        for val in count.values():
            result += (val * (val - 1)) // 2
        
        return result