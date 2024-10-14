from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        result = 0
        stack = []  # stack (index, value) of increasing values

        for i, num in enumerate(arr):
            while stack and stack[-1][1] > num:
                j, value = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j
                result = (result + value * left * right) % MOD
            stack.append((i, num))

        for i in range(len(stack)):
            j, value = stack[i]
            left = j - stack[i - 1][0] if i > 0 else j + 1
            right = len(arr) - j
            result = (result + value * left * right) % MOD

        return result
