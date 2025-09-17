class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            stack.append(c)
            while len(stack) >= 2 and (
                stack[-1].isdigit() and (not stack[-2].isdigit())
            ):
                stack.pop()
                stack.pop()
        return ''.join(stack)
