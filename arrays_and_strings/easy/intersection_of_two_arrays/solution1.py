from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        visited = set(nums1)
        result = []
        for n in nums2:
            if n in visited:
                result.append(n)
                visited.remove(n)
        
        return result