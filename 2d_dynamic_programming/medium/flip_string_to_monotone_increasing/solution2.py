class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        result = 0
        ones = 0

        for c in s:
            if c == '1':
                ones += 1
            else:
                result = min(result + 1, ones)

        return result
