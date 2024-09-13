from typing import List
from collections import defaultdict


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        result = []

        for num in nums:
            row = count[num]
            if len(result) == row:
                result.append([])

            result[row].append(num)
            count[num] += 1
        
        return result