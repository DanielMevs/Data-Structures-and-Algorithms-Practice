from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        result = 0
        arr = [float('-inf')] + arr + [float('-inf')]
        stack = []  # stack (index, value) of increasing values

        for i, num in enumerate(arr):
            while stack and stack[-1][1] > num:
                j, value = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j
                result = (result + value * left * right) % MOD
            stack.append((i, num))

        return result
