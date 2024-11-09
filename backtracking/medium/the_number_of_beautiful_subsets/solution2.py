from typing import List
from collections import Counter


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        groups = []  # of dicts
        visited = set()
        cache = {}

        def helper(num, group):
            if num not in group:
                return 1
            if num in cache:
                return cache[num]
            skip = helper(num + k, group)
            include = (2**group[num] - 1) * helper(num + 2 * k, group)
            cache[num] = skip + include
            return skip + include

        for num in count.keys():
            if num in visited:
                continue
            group = {}
            while num - k in count:
                num -= k
            while num in count:
                group[num] = count[num]
                visited.add(num)
                num += k

            groups.append(group)

        result = 1
        for group in groups:
            num = min(group.keys())
            result *= helper(num, group)

        return result - 1
