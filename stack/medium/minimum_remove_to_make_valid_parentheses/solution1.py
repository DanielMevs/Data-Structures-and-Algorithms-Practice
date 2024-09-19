class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = []
        count = 0  # extra open parentheses

        for char in s:
            if char == '(':
                result.append(char)
                count += 1
            elif char == ')' and count > 0:
                result.append(char)
                count -= 1
            elif char != ")":
                result.append(char)
        
        filtered = []
        for char in reversed(result):
            if char == '(' and count > 0:
                count -= 1
            else:
                filtered.append(char)

        return ''.join(reversed(filtered))
    