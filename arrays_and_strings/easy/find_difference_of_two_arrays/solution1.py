class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        return [list(set(n for n in nums1 if n not in nums2)), list(set(n for n in nums2 if n not in nums1))]