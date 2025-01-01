class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'}': '{', ']': '[', ')': '('}
        for i in range(len(s)):
            if stack and s[i] in [']', '}', ')']:
                if pairs[s[i]] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])

        return not stack
