from typing import List
from collections import defaultdict


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        def helper(i, count):
            if i == len(nums):
                return 1

            result = helper(i + 1, count)  # skip nums[i]
            if not count[nums[i] + k] and not count[nums[i] - k]:
                # include nums[i]
                count[nums[i]] += 1
                result += helper(i + 1, count)
                count[nums[i]] -= 1
            return result

        return helper(0, defaultdict(int)) - 1  # subtract empty subset
