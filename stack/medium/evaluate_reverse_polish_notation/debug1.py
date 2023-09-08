class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        result = 0


        while tokens:
            char = tokens.pop(0)
            
            if char.isdigit():
                print(f'char: {char}')
                stack.append(int(char))
                
            else:
                while stack:
                    val = stack.pop()
                    print(f'val: {val}')
                    if char == '+':
                        temp = result
                        result += val
                        print(f'Added {val} to {temp}')
                        print(f'New result: {result}')
                    elif char == '-':
                        temp = result
                        result -= val
                        print(f'Subtracted {val} from {temp}')
                        print(f'New result: {result}')
                    elif char == '*':
                        result *= val
                        print(f'Multiplied {val} to {temp}')
                        print(f'New result: {result}')
                    elif char == '/':
                        result /= val
                        print(f'Divided {val} by {temp}')
                        print(f'New result: {result}')
                    else:
                        raise Exception("Invalid operator")
            print(f'stack: {stack}')
        print(f'Final result: {result}')
        return result
    
Solution().evalRPN(tokens=["2","1","+","3","*"])