# removes duplicate elements from sorted array about shifting
# unique elements to the start of the array and returning the pointer

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left, right = 1, 1
        while right < len(nums):
            if nums[right - 1] < nums[right]:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left