import operator

ops = { 
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv
}

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        result = 0


        while tokens:
                              
            char = tokens.pop(0)

            # - Note: isdigit will produce false for negative numbers
            if char.isdigit():
                stack.append(int(char))

            else:
                
                num1, num2 = 0, 0
                for i in range(2):
                    if i + 1 == 1:
                        num2 = stack.pop()
                    else:
                        num1 = stack.pop()
                result = ops[char](num1, num2)
                stack.append(result)

        return stack.pop()