from typing import List
from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        result = 0
        count = defaultdict(int)
        left, right = 0, 0

        while right < len(nums):
            count[nums[right]] += 1
            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
            right += 1

        return result