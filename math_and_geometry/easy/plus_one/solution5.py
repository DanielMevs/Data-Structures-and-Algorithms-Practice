class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        def isNine(digit):
            return digit == 9
        
        if all(map(isNine, digits)):
            return [1] + [0 for _ in digits]
        
        i = len(digits) - 1

        while isNine(digits[i]):
            digits[i] = 0
            i -= 1
        
        digits[i] += 1
        return digits