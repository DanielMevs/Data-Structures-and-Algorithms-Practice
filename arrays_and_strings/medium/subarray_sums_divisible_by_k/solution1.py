from typing import List
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        prefix_sum = result = 0
        count[0] += 1

        for num in nums:
            prefix_sum += num
            remain = prefix_sum % k
            result += count[remain]  # defaults to 0
            count[remain] += 1

        return result
