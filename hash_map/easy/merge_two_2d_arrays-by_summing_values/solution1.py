from typing import List
from collections import defaultdict


class Solution:
    def mergeArrays(
            self, nums1: List[List[int]],
            nums2: List[List[int]]) -> List[List[int]]:
        nums_dict = defaultdict(int)
        for num1 in nums1:
            nums_dict[num1[0]] += num1[1]
        for num2 in nums2:
            nums_dict[num2[0]] += num2[1]
        return [[num1, num2] for num1, num2 in sorted(
            nums_dict.items(), key=lambda x: x[0])]
