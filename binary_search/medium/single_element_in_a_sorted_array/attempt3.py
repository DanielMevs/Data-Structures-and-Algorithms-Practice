class Solution:

    
    def singleNonDuplicate(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            curr = nums[mid]

            
            prev = False if mid - 1 <= 0 else nums[mid-1]
            
            next = False if mid + 1 < len(nums) else nums[mid+1]  
            
            
            result = (
                (prev or prev != curr) and 
                (next or curr != next)
            )

            if result:
                return curr
            
            leftSize = mid - 1 if prev == curr else mid
            if leftSize % 2:
                right = mid - 1
            else:
                left = mid + 1
