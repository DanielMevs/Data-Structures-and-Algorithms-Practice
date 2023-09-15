class Solution:

    
    def singleNonDuplicate(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while True:
            mid = left + ((right - left) // 2)
            
            prev = nums[mid-1]
            curr = nums[mid]
            next = nums[mid+1]
            
            if prev == curr:
                left = mid + 1
            elif curr == next:
                right = mid - 1
            else:
                return mid