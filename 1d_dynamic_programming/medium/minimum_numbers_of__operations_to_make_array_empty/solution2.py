from typing import List
from collections import Counter


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cache = {}
        
        def dfs(n):
            if n < 0:
                return float('inf')
            if n in [2, 3]:
                return 1
            if n in cache:
                return cache[n]
            
            result = min(dfs(n - 2), dfs(n - 3)) 
            if result == -1:
                return -1
            cache[n] = result + 1
            return result + 1
    
        count = Counter(nums)
        result = 0
        for num, cnt in count.items():
            op = dfs(cnt)
            if op == float('inf'):
                return -1
            result += op
        
        return result