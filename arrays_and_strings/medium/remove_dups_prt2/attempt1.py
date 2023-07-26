class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        right, left = 0, 0

        while right < len(nums):
            num = nums[left]
            freq = 1
            while nums[right] == num:
                if freq > 2:
                    right += 1
                    freq += 1
                else:
                    right += 1
                    left += 1
                    freq += 1
            i = right
            while i > left:
                nums[i], nums[i-1] = nums[i - 1], nums[i]
                i -= 1
            left = right


        return left