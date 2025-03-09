from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = bank[0].count('1')
        result = 0

        for i in range(1, len(bank)):
            curr = bank[i].count('1')
            if curr:
                result += (prev * curr)
                prev = curr

        return result
