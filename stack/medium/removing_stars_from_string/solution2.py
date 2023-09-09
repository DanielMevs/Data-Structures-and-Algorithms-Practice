class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char != '*':
                stack.append(char)
            else:
                # - Will not pop if the stack is empty
                stack and stack.pop()
        return ''.join(stack)