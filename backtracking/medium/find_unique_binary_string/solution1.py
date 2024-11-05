from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        strSet = set(nums)

        def backtrack(i, curr):
            if i == len(nums):
                result = ''.join(curr)
                return None if result in strSet else result
            result = backtrack(i + 1, curr)
            if result:
                return result

            curr[i] = '1'
            result = backtrack(i + 1, curr)
            if result:
                return result

        return backtrack(0, ['0'] * len(nums))
