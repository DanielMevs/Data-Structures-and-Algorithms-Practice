from collections import Counter
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        result = []

        for num in arr2:
            result += [num] * count.pop(num)

        for num in sorted(count):
            result += [num] * count[num]

        return result
