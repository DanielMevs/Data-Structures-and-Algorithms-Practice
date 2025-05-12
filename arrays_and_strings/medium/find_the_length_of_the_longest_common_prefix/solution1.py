from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        result = 0

        # We want arr1 to be the shorter list
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        # Add all prefix from the shorter list to a set
        prefix_set = set()
        for n in arr1:
            while n and n not in prefix_set:
                prefix_set.add(n)
                n //= 10

        # Look for the longest prefix in arr2
        for n in arr2:
            while n and n not in prefix_set:
                n //= 10
            if n:
                result = max(result, len(str(n)))

        return result
