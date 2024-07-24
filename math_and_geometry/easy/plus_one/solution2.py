class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        plusOne = int(''.join(str(n) for n in digits)) + 1
        return [int(x) for x in str(plusOne)]   