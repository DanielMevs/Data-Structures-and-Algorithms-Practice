class Solution:
    def reverse(self, x: int) -> int:
        
        result = 0
        isPos = x >= 0

        while x:
            result += abs(x) % 10
            x = int(x / 10)
            result *= 10

        if isPos:
            result = result // 10
        else:
            result = -int(result / 10)
                    
        return result if result in range(-2**31, 2**31) else 0