SAME_CHAR_ALT_CASE_ORD_DIFF = 32


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        def is_bad_pair(char1, char2):
            return abs(ord(char1) - ord(char2)) == SAME_CHAR_ALT_CASE_ORD_DIFF
        
        for char in s:
            if stack and is_bad_pair(stack[-1], char):
                stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)
    