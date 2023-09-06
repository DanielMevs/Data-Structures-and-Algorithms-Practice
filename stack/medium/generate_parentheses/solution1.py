# - Given n pairs of parentheses, write a function to 
# generate all combinations of well-formed parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # - Only add open parenthesis if open < n
        # - Only add a closing parenthesis if closed < open
        # - return if and only if open == close == n


        stack = []

        result = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                result.append(''.join(stack))
                return

            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0,0)
        return result

