class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        i = 0
        stack = []
        for num in pushed:
            stack.append(num)
            while i < len(popped) and stack and popped[i] == stack[-1]:
                stack.pop()
                i += 1
        return not stack