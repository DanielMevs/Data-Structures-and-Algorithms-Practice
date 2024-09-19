class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dvd = abs(dividend)
        dvs = abs(divisor)
        result = 0

        while dvd >= dvs:
            temp = dvs
            mult = 1
            while dvd >= temp:
                dvd -= temp
                result += mult
                temp += temp
                mult += mult

        if (dividend < 0 and divisor >= 0) or (
                dividend >= 0 and divisor < 0):
            result = -result
        
        return min(max(-2**31, result), 2**31 - 1)