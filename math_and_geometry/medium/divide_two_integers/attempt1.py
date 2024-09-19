class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dvd = abs(dividend)
        dvs = abs(divisor)
        result = 0

        while dvd >= dvs:
            dvd -= dvs
            result += 1
        
        if (dividend < 0 and divisor >= 0) or (
                dividend >= 0 and divisor < 0):
            result = -result
        
        return result