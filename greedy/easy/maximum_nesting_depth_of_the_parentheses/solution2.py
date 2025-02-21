class Solution:
    def maxDepth(self, s: str) -> int:
        result, current = 0, 0

        for c in s:
            if c == '(':
                current += 1
            elif c == ')':
                current -= 1
            result = max(result, current)

        return result
