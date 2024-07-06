class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}  # char -> last index in s

        for i, c in enumerate(s):
            lastIndex[c] = i

        result = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])
            if i == end:
                result.append(size)
                size = 0
        
        return result