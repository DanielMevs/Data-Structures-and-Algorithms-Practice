from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        result = 0
        stack = []
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)

        for i, n in enumerate(nums):
            newStart = i
            while stack and stack[-1][1] > n:
                start, value = stack.pop()
                result = max(result, value * (prefix[i] - prefix[start]))
                newStart = start
            stack.append((newStart, n))

        for start, val in stack:
            result = max(result, val * (prefix[len(nums)] - prefix[start]))

        return result % (10 ** 9 + 7)
