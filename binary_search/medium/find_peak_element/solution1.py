class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + ((right - left)//2)
            # - Is left neighbor greater?
            if mid > 0 and nums[mid] < nums[mid-1]:
                right = mid - 1
            # - Is right neighbor greater?
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                return mid