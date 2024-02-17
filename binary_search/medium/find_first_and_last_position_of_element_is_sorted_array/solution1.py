class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]
    
    # - leftBias[True/False], if false, result is rightBiased
    def binSearch(self, nums, target, leftBias):
        left, right = 0, len(nums) - 1
        i = -1
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                i = mid
                if leftBias:
                    right = mid - 1
                else:
                    left = mid + 1
        return i