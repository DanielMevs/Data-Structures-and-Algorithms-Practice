class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        right = 0

        while right < len(nums):
            num = nums[right]
            freq = 1
            while nums[right] == num and right < len(nums):
                    freq += 1
                    right += 1
            left = right - freq
            nums[left] = num
            nums[left + 1] = num

        return left + 1


