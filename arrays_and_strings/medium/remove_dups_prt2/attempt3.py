class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        right = 0
        left = 0

        while right < len(nums):
            freq = 1
            while nums[right] == nums[right + 1] and right + 1 < len(nums):
                freq += 1
                right += 1
            for _ in range(min(2, freq)):
                nums[left] = nums[right]
                left += 1

            right += 1
            

        return left


