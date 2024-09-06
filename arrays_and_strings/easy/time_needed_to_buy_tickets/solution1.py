from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0

        for i in range(len(tickets)):
            if i <= k:
                result += min(tickets[i], tickets[k])
            else:
                result += min(tickets[i], tickets[k] - 1)

        return result
    
