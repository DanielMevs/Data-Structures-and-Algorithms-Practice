from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remain = total % p

        if not remain:
            return 0

        result = len(nums)
        run_sum = 0
        remain_to_idx = {0: -1}

        for i, num in enumerate(nums):
            run_sum = (run_sum + num) % p
            target = (run_sum - remain + p) % p
            if target in remain_to_idx:
                length = i - remain_to_idx[target]
                result = min(result, length)
            remain_to_idx[run_sum] = i

        return -1 if result == len(nums) else result
