from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda p: p[1])
        longestChain = 1
        end = pairs[0][1]
        for i in range(1, len(pairs)):
            if end < pairs[i][0]:
                longestChain += 1
                end = pairs[i][1]

        return longestChain
