#  - Runtime: O(n * 2^n); n = length of nums
from collections import Counter


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = []
        perm = []
        count = Counter(nums)

        def dfs():
            if len(perm) == len(nums):
                result.append(perm.copy())
                return
            for n in count:
                # - Only perform if count[n] is not 0
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1

                    dfs()

                    count[n] += 1
                    perm.pop()
        dfs()
        return result
