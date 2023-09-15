class Solution:

    
    def singleNonDuplicate(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            
            prev = nums[mid-1]
            curr = nums[mid]
            next = nums[mid+1]
            
            
            if curr == next or prev == curr:
                if len(nums[next+1:]) % 2 == 0:
                    right = prev
                else:
                    left = next
            else:
                return mid