class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = [c for c in s]
        left = 0

        for right in range(len(s)):
            if s[right] == '1':
                s[right], s[left] = s[left], s[right]
                left += 1
        s[left - 1], s[-1] = s[-1], s[left - 1]

        return ''.join(s)
