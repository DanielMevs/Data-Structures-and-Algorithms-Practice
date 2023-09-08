class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        result = 0


        while tokens:
                              
            char = tokens.pop()
            if char.isdigit():
                stack.append(int(char))
            else:
                while stack:
                    if char == '+':
                        result += stack.pop()
                    elif char == '-':
                        result -= stack.pop()
                    elif char == '*':
                        result *= stack.pop()
                    elif char == '/':
                        result /= stack.pop()
                    else:
                        raise Exception("Invalid operator")
        return result