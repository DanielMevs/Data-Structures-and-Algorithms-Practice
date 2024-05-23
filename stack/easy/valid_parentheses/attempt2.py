class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braceOrder = {
            '[': ']',
            '{': '}',
            '(': ')'
        }
        for char in s:
            if stack and braceOrder[stack[-1]] == char:
                stack.pop()
            elif stack and char not in braceOrder.keys():
                return False
            elif char in braceOrder.keys():
                stack.append(char)
            elif not stack and char in braceOrder.values():
                return False
            
        return True if not stack else False