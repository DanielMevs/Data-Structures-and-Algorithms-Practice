class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == '-':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2 - num1)
            elif char == '*':
                stack.append(stack.pop() * stack.pop())
            elif char == '/':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(num2 / num1))
            else:
                stack.append(int(char))
        
        return stack.pop()