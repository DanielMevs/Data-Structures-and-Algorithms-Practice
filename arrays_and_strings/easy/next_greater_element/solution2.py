class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        numsOneIdx = {n:i for i, n in enumerate(nums1)}
        next_greater = [-1] * len(nums1)
        for i in range(len(nums2)):
            if nums2[i] not in numsOneIdx:
                continue
            for j in range(i, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = numsOneIdx[nums2[i]]
                    next_greater[idx] = nums2[j]
                    break
        
        return next_greater