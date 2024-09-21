from collections import Counter
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return list(filter(lambda x: count.get(x) == 2, count.keys()))