from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        townsPeople = {i: 0 for i in range(1, n+1)}
        for truster, trustee in trust:
            townsPeople[trustee] += 1
            townsPeople[truster] -= 1
        for person, trustee in townsPeople.items():
            if trustee == n - 1:
                return person
        return -1
