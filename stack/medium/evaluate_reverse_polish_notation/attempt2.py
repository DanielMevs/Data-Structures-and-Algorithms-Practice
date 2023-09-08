class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        result = 0
        first_operation = True


        while tokens:
                              
            char = tokens.pop(0)
            if char.isdigit():
                stack.append(int(char))

            else:
                while stack:
                    if char == '+':
                        result += stack.pop()
                        first_operation = False
                    elif char == '-':
                        result -= stack.pop()
                        first_operation = False
                    elif char == '*':
                        if first_operation:
                            result = 1
                        result *= stack.pop()
                        first_operation = False
                    elif char == '/':
                        if first_operation:
                            result = 1
                        result = stack.pop() / result
                        first_operation = False
                    else:
                        raise Exception("Invalid operator")
        return result