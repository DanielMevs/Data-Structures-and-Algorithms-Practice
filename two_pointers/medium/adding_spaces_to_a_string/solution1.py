from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ''
        s_idx = 0
        n, m = len(s), len(spaces)

        for i in range(n):
            if s_idx < m and i == spaces[s_idx]:
                result += ' '
                s_idx += 1
            result += s[i]

        return result
