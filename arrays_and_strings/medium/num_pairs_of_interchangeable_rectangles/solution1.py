class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        count = {} # mapping width to height ratio to the count of that ratio

        for width, height in rectangles:
            count[width / height] = count.get(width / height, 0) + 1
        
        result = 0
        for val in count.values():
            if val > 1:
                result += (val * (val - 1)) // 2
        
        return result
