class Solution:

    
    def singleNonDuplicate(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            
            curr = nums[mid]
            
            result = (
                (mid - 1 < 0 or nums[mid - 1] != curr) and 
                (mid + 1 == len(nums) or curr != nums[mid + 1])
            )

            if result:
                return curr
            
            leftSize = mid - 1 if nums[mid -1] == curr else mid
            if leftSize % 2:
                right = mid - 1
            else:
                left = mid + 1
