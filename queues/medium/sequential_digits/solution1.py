from typing import List
from collections import deque


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        queue = deque(range(1, 10))
        
        while queue:
            num = queue.popleft()
            
            if low <= num <= high:
                result.append(num)
            
            last_digit = num % 10
            if last_digit < 9:
                queue.append(num * 10 + last_digit + 1)

        return result