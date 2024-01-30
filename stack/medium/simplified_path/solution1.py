class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        current = ''

        for char in path + '/':
            if char == '/':
                if current == '..':
                    stack and stack.pop()
                elif current != '' and current != '.':
                    stack.append(current)
                current = ''
            else:
                current += char
        
        return '/' + '/'.join(stack)