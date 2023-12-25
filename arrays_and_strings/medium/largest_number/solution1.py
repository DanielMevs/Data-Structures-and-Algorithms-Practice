from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)
        
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            elif n1 < n2:
                return 1
            else:
                return 0

        nums = sorted(nums, key=cmp_to_key(compare))

        return str(int(''.join(nums)))