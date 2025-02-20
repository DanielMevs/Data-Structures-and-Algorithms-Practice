class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0  # count of ones
        for c in s:
            if c == '1':
                count += 1
        return (count - 1) * '1' + (len(s) - count) * '0' + '1'
