class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        current_sum = 0
        max_window = -1
        left = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while left <= right and current_sum > target:
                current_sum -= nums[left]
                left += 1

            if current_sum == target:
                max_window = max(max_window, right - left + 1)
            

        return -1 if max_window == -1 else len(nums) - max_window