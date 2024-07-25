import math


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num, result = 0, []
        n = len(digits)
        for i in range(n, 0, -1):
            num += digits[n - i] * (10 ** (i - 1))
        
        num += 1
        n = int(math.log10(num)) + 1
        for i in range(n - 1, -1, -1):
            sigFig = num // (10 ** (i))
            result.append(sigFig)
            num %= (10 ** (i))

        return result