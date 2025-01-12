from typing import List
from math import gcd
from collections import defaultdict


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        cache = defaultdict(int)

        def dfs(mask, op):
            if mask in cache:
                return cache[mask]

            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if (1 << i) & mask or (1 << j) & mask:
                        continue
                    newMask = mask | (1 << i) | (1 << j)
                    score = op * gcd(nums[i], nums[j])
                    cache[mask] = max(
                        score + dfs(newMask, op + 1),
                        cache[mask]
                    )
            return cache[mask]
        return dfs(0, 1)
