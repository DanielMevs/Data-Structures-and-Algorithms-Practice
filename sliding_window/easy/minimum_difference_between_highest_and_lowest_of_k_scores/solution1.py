from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_diff = float('inf')
        nums.sort()
        left, right = 0, k - 1

        while right < n:
            curr_diff = nums[right] - nums[left]
            min_diff = min(curr_diff, min_diff)
            left, right = left + 1, right + 1
        return min_diff
