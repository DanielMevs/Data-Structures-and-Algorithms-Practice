class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        # - This stack will store a pair: (index, height)
        stack = []

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                index, temp_height = stack.pop()
                maxArea = max(maxArea, (i - index) * temp_height)
                start = index
            stack.append((start, height))
        for i, height in stack:
            maxArea = max(maxArea, (len(heights) - i) * height)
        
        return maxArea
            