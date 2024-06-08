class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stackFuncs = {
            '+': lambda x, y: x + y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x/y),
            '-': lambda x, y: x - y
        }
        stack = []

        for token in tokens:
            if token in stackFuncs:
                op = stackFuncs[token]
                num2 = stack.pop()
                num1 = stack.pop()
                
                stack.append(op(num1, num2))
            else:
                stack.append(int(token))
        
        return stack.pop()
        