class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = [-1]*len(nums1)
        for num in nums1:
            idx = nums2.index(num)
            for i in range(idx, idx + len(nums2[idx:])):
                if nums2[i] > num:
                    next_greater[nums1.index(num)] = nums2[i]
                    break
        
        return next_greater
