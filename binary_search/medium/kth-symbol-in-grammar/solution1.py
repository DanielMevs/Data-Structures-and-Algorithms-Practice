class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        current = 0
        left, right = 1, 2 ** (n - 1)
        
        for _ in range(n - 1):
            mid = (left + right) // 2
            
            if k > mid:
                current = 1 - current
                k -= mid
                left = mid + 1
            else:
                right = mid
        
        return current