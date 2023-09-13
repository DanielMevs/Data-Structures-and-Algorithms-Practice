'''
Given a sorted array of distinct integers and a target value, return the index if 
the target is found. If not, return the index where it would be if it were 
inserted in order.
'''

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        
        return left