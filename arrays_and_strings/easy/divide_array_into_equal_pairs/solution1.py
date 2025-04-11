from collections import defaultdict
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        return all(not num % 2 for num in count.values())
