from typing import List
from collections import Counter
from math import ceil


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        result = 0
        for num, cnt in count.items():
            if cnt == 1:
                return -1
            result += ceil(cnt / 3)

        return result