from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        a1, a2 = 0, float('inf')
        for freq in count.values():
            if freq % 2 == 1:
                a1 = max(a1, freq)
            else:
                a2 = min(a2, freq)
        return a1 - a2
