class Solution:
    def maxDepth(self, s: str) -> int:
        max_open, open_count = 0, 0

        for c in s:
            if c == '(':
                open_count += 1
                max_open = max(open_count, max_open)
            if c == ')' and open_count:
                open_count -= 1

        return max_open - open_count
