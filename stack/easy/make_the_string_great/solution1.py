ALT_CASE__DIFF = 32


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        def is_bad_pair(char1, char2):
            return abs(ord(char1) - ord(char2)) == ALT_CASE__DIFF

        def is_bad_pair_v2(char1, char2):
            return char1 != char2 and char1.lower() == char2.lower()

        for char in s:
            if stack and is_bad_pair(stack[-1], char):
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)
