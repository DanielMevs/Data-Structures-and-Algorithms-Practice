class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        result = ['0'] * len(s)
        one = 0
        for c in s:
            if c == '1':
                one += 1
        result[-1], one = '1', one - 1
        for i in range(one):
            result[i] = '1'
        return ''.join(result)
