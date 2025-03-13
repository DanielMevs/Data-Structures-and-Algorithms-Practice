class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(lambda pair: pair[0])
        result = intervals[0]

        for start, end in intervals[1:]:
            lastEnd = result[-1][1]
            if start <= lastEnd:
                result[-1][1] = max(end, lastEnd)
            else:
                result.append([start, end])
        
        return result