from typing import List
from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count, lucky = Counter(arr), -1
        for num, count in count.items():
            if num == count:
                lucky = max(num, lucky)
        return lucky
