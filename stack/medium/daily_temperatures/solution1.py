class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0]*len(temperatures)
        stack = []

        for i, num in enumerate(temperatures):

            while stack and num > stack[-1][0]:
                stackNum, stackIdx = stack.pop()
                answer[stackIdx] = (i - stackIdx)
            stack.append([num, i])
        
        return answer