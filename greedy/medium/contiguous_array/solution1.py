from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, one = 0, 0
        result = 0

        diff_index = {}  # count[1] - count[0] -> index

        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1
            
            if one - zero not in diff_index:
                diff_index[one - zero] = i
            if one == zero:
                result = one + zero
            else:
                idx = diff_index.get(one - zero)
                result = max(result, i - idx)
        
        return result
