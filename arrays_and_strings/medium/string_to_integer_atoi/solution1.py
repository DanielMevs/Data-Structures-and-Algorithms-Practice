class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31

        result = 0
        sign = 1
        index = 0

        # Remove leading whitespaces
        while index < len(s) and s[index].isspace():
            index += 1

        # Check if the number is negative
        if index < len(s) and s[index] == '-':
            sign = -1
            index += 1
        elif index < len(s) and s[index] == '+':
            index += 1
        
        # Build the result
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1

        result *= sign
        return max(MIN_INT, min(MAX_INT, result))