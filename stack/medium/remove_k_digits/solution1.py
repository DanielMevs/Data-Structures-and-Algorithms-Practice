class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for char in num:
            while k > 0 and stack and stack[-1] > char:
                k -= 1
                stack.pop()
            if stack or char is not '0':
                stack.append(char)
        
        # - Accounting for the case where k is still a positive
            # number, meaning we haven't popped all k values
            # we were looking to pop
        if k:
            stack = stack[:- k]


        return ''.join(stack) or '0'
